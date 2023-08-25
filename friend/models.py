from django.db import models
from django.contrib.auth.models import User


""" FriendList model """
class FriendList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    friends = models.ManyToManyField(User, blank=True, related_name='friends')
    
    def friends_data(self):
        return [str(p) for p in self.friends.all()]
    def __str__(self):
        # return f'{self.user.username} --> {self.friends.all}'
        return f'{self.user.username} --> {[str(p) for p in self.friends.all()]}'


""" Friend Request model """
class FriendRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    is_active = models.BooleanField(blank=True, null=True, default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.username} --> {self.receiver.username}'
