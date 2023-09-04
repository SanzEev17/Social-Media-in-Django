from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from .models import Profile
from friend.models import FriendList, FriendRequest
from .forms import ProfileForm
from post.models import Post, Comments, Likes
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
@login_required
def user_profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    friends = FriendList.objects.get(user=request.user)
    friend_requests = FriendRequest.objects.all()
    friend_request_sent = friend_requests.filter(sender=request.user).filter(receiver=user)
    friend_request_received = friend_requests.filter(sender=user).filter(receiver=request.user)
    posts = Post.objects.annotate(comment_count=Count('comments')).filter(user=user)
    comments = Comments.objects.all()
    likes = Likes.objects.all().filter(user=request.user)
    # profile_form = ProfileForm(instance=profile)


    context = {
        'friends':friends,
        "profile_data" : profile,
        'friend_request_sent':friend_request_sent,
        'friend_request_received':friend_request_received,
        'posts':posts,
        'comments':comments,
        'likes':likes,
        # 'profile_form':profile_form
    }
    return render(request, 'user-profile/user-profile.html', context=context)


@login_required
def create_profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    context = {
        'form':profile_form,
    }
    if profile_form.is_valid():
        profile_form.save()
        return redirect("user_profile", username=request.user)
    return render(request, 'user-profile/create-update-profile.html', context)