from django.urls import path
from . import views

urlpatterns = [
    path('', views.friends_list, name='friends_list'),
    path('requests/', views.friend_requests, name='friend_requests'),
    path('send_friend_request/<str:username>', views.send_friend_request, name='send_friend_request'),
    path('cancel_friend_request/<int:friend_request_id>', views.cancel_friend_request, name='cancel_friend_request'),
    path('accept_friend_request/<int:friend_request_id>', views.accept_friend_request, name='accept_friend_request'),
    path('decline_friend_request/<int:friend_request_id>', views.decline_friend_request, name='decline_friend_request'),
    path('unfriend/<str:username>', views.unfriend, name='unfriend'),
]
