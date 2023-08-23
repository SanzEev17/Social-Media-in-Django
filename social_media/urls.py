from django.contrib import admin
from django.urls import path, include
from .views import base_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_view, name='base'),
    path('', include('accounts.urls')),
    path('', include('feed.urls')),
    path('', include('user_profile.urls')),
]
