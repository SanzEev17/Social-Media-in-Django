from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'type':'password',
    }))
    class Meta:
        model = User
        fields = ["username", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_data = {
                'class':'form-control form-control-lg',
                'id': str(field),
                'label':field.capitalize()
            }
            self.fields[str(field)].widget.attrs.update(new_data)



class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'autofocus':'True'
    }), label='First Name')
    last_name = forms.CharField(widget=forms.TextInput(), label='Last Name')
    username = forms.CharField(widget=forms.TextInput(), label='Username')
    email = forms.EmailField(widget=forms.TextInput(), label='Email Address')
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'type':'password',
    }), label='Password')
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'type':'password',
    }), label='Confirm Password')
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_data = {
                'class':'form-control form-control-lg',
                'id': str(field),
            }
            self.fields[str(field)].widget.attrs.update(new_data)