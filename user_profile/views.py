from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

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