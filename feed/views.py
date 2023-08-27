from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from friend.models import FriendList

@login_required
# Create your views here.
def home_view(request):
    friends = FriendList.objects.get(user=request.user)
    print(friends)
    context = {
        'friends':friends
    }
    return render(request, 'feed/home.html', context)