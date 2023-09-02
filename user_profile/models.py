from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='profile_images', default='default.png')
    bio = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=50, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username