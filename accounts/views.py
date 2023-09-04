from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm

# Create your views here.
def login_view(request):
    # context = {}
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')

    else:
        form = LoginForm(request, )
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    context = {}
    if request.method == "POST":
        logout(request)
        return redirect('accounts:login')
    return render(request, 'accounts/logout.html', context=context)


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user_save = form.save()
        return redirect("accounts:login")

    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context=context)
