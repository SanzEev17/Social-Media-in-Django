from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from friend.models import FriendList
from post.models import Post, Comments
from post.forms import PostForm,CommentForm

@login_required
# Create your views here.
def home_view(request):
    friends = FriendList.objects.get(user=request.user)
    # posts = Post.objects.all()
    posts = Post.objects.annotate(comment_count=Count('comments'))
    comments = Comments.objects.all()
    post_form = PostForm()
    comment_form = CommentForm()
    
    context = {
        'friends':friends,
        'posts':posts,
        'post_form':post_form,
        'comments':comments,
        'comment_form':comment_form
    }
    return render(request, 'feed/home.html', context)

def create_post(request):
    post_form = PostForm(request.POST)
    if post_form.is_valid():
        obj = post_form.save(commit=False)
        obj.user = request.user
        obj.save()
    return redirect('/')


def create_comment(request):
    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        obj = comment_form.save(commit=False)
        obj.post.id=request.POST.get('post')
        obj.commenter = request.user
        obj.save()
    return redirect('/')