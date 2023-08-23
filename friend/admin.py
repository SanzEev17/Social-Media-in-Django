from django.contrib import admin
from .models import FriendList, FriendRequest

# Register your models here.
class FriendListAdmin(admin.ModelAdmin):
    list_filter = ['user']
    list_display = ['user']
    search_fields= ['user']
    readonly_fields = ['user']

admin.site.register(FriendList, FriendListAdmin)


class FriendRequestAdmin(admin.ModelAdmin):
    list_filter = ['sender', 'receiver']
    list_display = ['sender', 'receiver']
    search_fields= ['sender__username', 'receiver__username']

admin.site.register(FriendRequest, FriendRequestAdmin)