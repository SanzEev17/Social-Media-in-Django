from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class FriendList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField(User, blank=True, related_name='friends')


    def __str__(self):
        self.user.username

    def add_friend(self, account):
        if not account in self.friends.all():
            self.friends.add(account)
    
    def remove_friend(self, account):
        if account in self.friends.all():
            self.friends.remove(account)

    def unfriend(self, removed):
        #Removed is the person who gets unfriended
        remover = self #The person who unfriends the removed
        remover.remove_friend(removed)
        friends_list = FriendList.objects.get(user=removed)
        friends_list.remove_friend(remover.user)#Removing me from other persons friend list

    def are_we_friends(self, friend):
        if friend in self.friends.all():
            return True
        else:
            return False


class FriendRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    is_active = models.BooleanField(null=True, blank=True, default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.username
    
    def accept_request(self):
        receiver_friend_list = FriendList.objects.get(user=self.receiver)
        if receiver_friend_list:
            sender_friend_list = FriendList.objects.get(user=self.sender)
            if sender_friend_list:
                sender_friend_list.add_friend(self.receiver)
                self.save()

    def decline_request(self):
        self.is_active=False
        self.save()

    def cancel_request(self):
        self.is_active=False
        self.save()
