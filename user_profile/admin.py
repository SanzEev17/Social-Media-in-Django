from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

# Register your models here.

admin.site.unregister(Group)


class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model=User
    fields = ['first_name','last_name','username', 'email', 'password']
    inlines = [ProfileInline,]

admin.site.register(User, UserAdmin)