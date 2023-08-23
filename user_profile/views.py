from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
@login_required
def user_profile_view(request):
    print(request.user)
    profile = Profile.objects.get(user=request.user)
    print(profile.address)
    context = {
        "profile_data":profile
    }
    return render(request, 'user-profile/user-profile.html', context=context)