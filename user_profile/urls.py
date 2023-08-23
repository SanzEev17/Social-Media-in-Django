from django.urls import path
from .views import(
    user_profile_view
)
app_name = "feed"
urlpatterns = [
    path('profile/', user_profile_view, name='user_profile')
]

