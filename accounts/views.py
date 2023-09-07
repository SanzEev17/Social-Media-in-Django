from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
import pyotp
from django.core.mail import send_mail
from .forms import LoginForm, RegisterForm, OTPVerificationForm
from django.contrib.auth.views import PasswordResetView
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()

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
        totp = pyotp.TOTP(pyotp.random_base32())
        otp = totp.now()
        send_mail(
                'Your OTP',
                f'Your OTP for registration is: {otp}',
                'pearljam171@outlook.com',
                [form.cleaned_data['email']],
                fail_silently=False,
            )
        request.session['registration_data'] = {
                'otp': otp,
                'form_data': form.cleaned_data,
            }
        # user_save = form.save()
        return redirect("accounts:verify_otp")

    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context=context)



def verify_otp(request):
    form = OTPVerificationForm(request.POST)
    registration_data = request.session.get('registration_data')
    if form.is_valid():
        user_otp = form.cleaned_data['otp']
        if user_otp == registration_data['otp']:
            del request.session['registration_data']
            user = User.objects.create_user(
                first_name = registration_data['form_data']['first_name'],
                last_name = registration_data['form_data']['last_name'],
                username=registration_data['form_data']['username'],
                email=registration_data['form_data']['email'],
                password=''  # Leave password empty for now
            )
            user.set_password(registration_data['form_data']['password1'])
            user.save()
            return redirect('accounts:login')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
    context = {
        'form':form
    }
    return render(request, 'accounts/verify-otp.html', context)

class ResetPasswordView(PasswordResetView):
    from_email = 'pearljam171@outlook.com'
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."