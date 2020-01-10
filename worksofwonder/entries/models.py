
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Articles(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    date_posted= models.DateTimeField(default=timezone.now)  # use auto_now_add=True
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if a user is deleted, delete post as well

    def __str__(self):
        return self.name