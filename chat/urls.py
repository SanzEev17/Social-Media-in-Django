from django.urls import path
from . import views

app_name = "chat"
urlpatterns = [
    path('', views.chat_list, name='chat_list'),
    path('<int:request_id>/', views.chat, name='chat'),
    path('send_message/', views.send_message, name='send_message'),
]
