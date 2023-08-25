from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from friend.models import FriendList, FriendRequest
from .forms import ProfileForm

# Create your views here.
@login_required
def user_profile_view(request, username=None):
    user=None
    profile=None
    if username is not None:
        try:
            user = User.objects.get(username=username)
            profile = Profile.objects.get(user=user)
            friends = FriendList.objects.filter(user=request.user)
            friend_requests = FriendRequest.objects.all()
            friend_request_sent = friend_requests.filter(sender= request.user).filter(receiver=user)
            friend_request_received = friend_requests.filter(sender=user).filter(receiver=request.user)
        except:
            profile = None
    context = {
        'friends':friends,
        "profile_data" : profile,
        'friend_request_sent':friend_request_sent,
        'friend_request_received':friend_request_received
    }
    return render(request, 'user-profile/user-profile.html', context=context)


@login_required
def create_profile_view(request):
    form = ProfileForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
    return render(request, "user-profile/create-update-profile.html", context=context)