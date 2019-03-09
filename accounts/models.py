from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile')
    bio = models.TextField()
    facebook = models.URLField(max_length=255)
    www = models.URLField(max_length=255)

    def __str__(self):
        return self.user.username