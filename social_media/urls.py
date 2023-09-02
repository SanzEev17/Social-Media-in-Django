from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import base_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('feed.urls')),
    path('', include('post.urls')),
    path('friends/', include('friend.urls')),
    path('', include('user_profile.urls')),
    path('chat/', include('chat.urls')),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
