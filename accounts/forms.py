from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control form-control-lg',
        'id':'username',
    }), label='Username')
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control form-control-lg',
        'id':'password',
        'type':'password',
    }), label='Password')
    class Meta:
        model = User
        fields = ["username", "password"]


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control form-control-lg',
        'id':'fname',
        'autofocus':'True'
    }), label='First Name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control form-control-lg',
        'id':'lname',
    }), label='Last Name')
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control form-control-lg',
        'id':'username',
    }), label='Username')
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control form-control-lg',
        'id':'email',
    }), label='Email Address')
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control form-control-lg',
        'id':'password1',
        'type':'password',
    }), label='Password')
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control form-control-lg',
        'id':'password2',
        'type':'password',
    }), label='Confirm Password')
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'username', 'email', 'password1', 'password2']