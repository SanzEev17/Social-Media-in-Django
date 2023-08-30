from django.shortcuts import render, redirect
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