from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    # USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.username