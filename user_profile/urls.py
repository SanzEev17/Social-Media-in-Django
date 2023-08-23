from django.urls import path
from .views import(
    user_profile_view,
    create_profile_view
)

urlpatterns = [
    path('profile/', user_profile_view, name='user_profile'),
    path('create/', create_profile_view, name='add_profile')
]

