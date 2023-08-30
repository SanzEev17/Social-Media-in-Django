from django.urls import path
from .views import(
    home_view,
    create_post,
    create_comment
)

urlpatterns = [
    path('', home_view, name='home'),
    path('create_post', create_post, name='create_post'),
    path('comment', create_comment, name='comment'),
]

