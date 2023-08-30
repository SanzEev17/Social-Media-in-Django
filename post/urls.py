from django.urls import path
from .views import(
    create_post,
    create_comment
)

urlpatterns = [
    path('create_post', create_post, name='create_post'),
    path('create_comment', create_comment, name='create_comment'),
]

