from django.shortcuts import render, redirect
from .models import Post, Likes
from .forms import PostForm,CommentForm

# Create your views here.
def create_post(request):
    post_form = PostForm(request.POST, request.FILES)
    if post_form.is_valid():
        obj = post_form.save(commit=False)
        obj.user = request.user
        obj.save()
    return redirect('/')


def create_comment(request):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        obj = comment_form.save(commit=False)
        obj.post.id=request.POST.get('post')
        obj.commenter = request.user
        obj.save()
    return redirect('/')

def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    current_likes = post.no_of_likes
    is_liked = Likes.objects.filter(user=request.user, liked_post=post)
    if not is_liked:
        is_liked = Likes.objects.create(user=request.user, liked_post=post)
        current_likes += 1
    else:
        is_liked = Likes.objects.filter(user=request.user, liked_post=post).delete()
        current_likes -= 1
    post.no_of_likes=current_likes
    post.save()
    return redirect('/')