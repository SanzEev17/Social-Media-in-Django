from django.urls import path
from .views import(
    create_post,
    create_comment,
    like_post
)
app_name='post'
urlpatterns = [
    path('create_post', create_post, name='create_post'),
    path('create_comment', create_comment, name='create_comment'),
    path('<int:post_id>/like', like_post, name='like_post')
]

