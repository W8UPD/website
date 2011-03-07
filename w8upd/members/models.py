from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    picture_url = models.URLField(max_length=255)
    major = models.CharField(max_length=255)
    biography = models.TextField()
