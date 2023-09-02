from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
def img_path(instance, filename):
    return f"post_by_{instance.user.username}/{filename}"


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_photo = models.ImageField(upload_to=img_path, null=True, blank=True)
    caption = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.commenter.username} commented {self.comment}"
    


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='liked_post', null=True)
    
    def __str__(self):
        return self.user.first_name