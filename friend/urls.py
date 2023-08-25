from django.urls import path

from . import views

urlpatterns = [
    path('', views.friends_list, name='friends_list'),
    path('send_friend_request/<str:username>', views.send_friend_request, name='send_friend_request'),
    path('cancel_friend_request/<int:friend_request_id>', views.cancel_friend_request, name='cancel_friend_request'),
    path('accept_friend_request/<int:friend_request_id>', views.accept_friend_request, name='accept_friend_request'),
    path('unfriend/<str:username>', views.unfriend, name='unfriend'),
]
