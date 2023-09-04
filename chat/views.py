from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Message
from friend.models import FriendList
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

def chat_list(request):
    friends = FriendList.objects.get(user=request.user)
    messages = Message.objects.filter(
            Q(sender=request.user) | Q(receiver=request.user)
        ).order_by("timestamp")
    friend_messages = []
    for friend in friends.friends.all():
        messages = Message.objects.filter(
            Q(sender=request.user, receiver=friend) | Q(sender=friend, receiver=request.user)
        ).order_by("-timestamp").first()
        friend_messages.append((friend, messages))

    context = {
        'friends':friends,
        'friend_messages':friend_messages
    }
    return render(request, 'chat/chat-list.html', context)

def chat(request, request_id):
    receiver = User.objects.get(id=request_id)
    # messages = Message.objects.filter(sender=request.user, receiver=receiver) | Message.objects.filter(sender=receiver, receiver=request.user)
    messages = Message.objects.filter(
            Q(sender=request.user, receiver=receiver) | Q(sender=receiver, receiver=request.user)
        ).order_by("timestamp")
    return render(request, 'chat/chat.html', {'receiver': receiver, 'messages': messages})

def send_message(request):
    if request.method == 'POST':
        content = request.POST.get('content', None)
        receiver_id = request.POST.get('receiver_id', None)
        if content and receiver_id:
            receiver = User.objects.get(id=receiver_id)
            Message.objects.create(sender=request.user, receiver=receiver, content=content)
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})