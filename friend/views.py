from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import FriendList, FriendRequest


@login_required
def friends_list(request):
    friends = FriendList.objects.filter(user=request.user) | FriendList.objects.filter(friends=request.user)
    return render(request, 'user-profile/user-profile.html', {'friends': friends})


@login_required
def send_friend_request(request, username):
    user = User.objects.get(username=username)
    friend_request = FriendRequest.objects.create(
        sender=request.user, receiver=user
    )
    # return redirect('profile', user_id=user_id)
    return redirect('user_profile', username=user)


@login_required
def cancel_friend_request(request, friend_request_id):
    friend_request = FriendRequest.objects.get(id=friend_request_id)
    receiver = friend_request.receiver
    user = User.objects.get(username=receiver)
    friend_request.delete()
    return redirect('user_profile', username=user)


@login_required
def accept_friend_request(request, friend_request_id):
    friend_request = FriendRequest.objects.get(id=friend_request_id)
    try:
        receiver_friend_list = FriendList.objects.get(user=friend_request.receiver)
        sender_friend_list = FriendList.objects.get(user=friend_request.sender)
    except:
        receiver_friend_list = FriendList.objects.create(user=friend_request.receiver)
        sender_friend_list = FriendList.objects.create(user=friend_request.sender)
    # FriendList.objects.create(
    #     user=friend_request.sender, friends=friend_request.receiver
    # )
    receiver_friend_list.friends.add(friend_request.sender)
    sender_friend_list.friends.add(friend_request.receiver)
    friend_request.delete()
    return redirect('user_profile', username=friend_request.sender)


@login_required
def unfriend(request, username):
    user = User.objects.get(username=username)
    unfriender = FriendList.objects.get(user=request.user)
    unfriended = FriendList.objects.get(user=user)
    unfriender.friends.remove(user)
    unfriended.friends.remove(request.user)
    # friend = FriendList.objects.get(user=request.user, friends=user)
    # friend.delete()
    return redirect('user_profile', username=username)
