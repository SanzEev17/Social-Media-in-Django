from django.urls import path
from .views import(
    user_profile_view,
    create_profile_view
)

urlpatterns = [
    path('update/', create_profile_view, name='update_profile'),
    path('<str:username>/', user_profile_view, name='user_profile'),
]

