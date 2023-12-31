from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from friend.models import FriendList
from post.models import Post, Comments, Likes
from post.forms import PostForm,CommentForm

@login_required
# Create your views here.
def home_view(request):
    friends = FriendList.objects.get(user=request.user)
    posts = Post.objects.annotate(comment_count=Count('comments'))
    comments = Comments.objects.all()
    likes = Likes.objects.all().filter(user=request.user)
    post_form = PostForm()
    comment_form = CommentForm()
    
    context = {
        'friends':friends,
        'posts':posts,
        'post_form':post_form,
        'comments':comments,
        'comment_form':comment_form,
        'likes':likes
    }
    return render(request, 'feed.html', context)

