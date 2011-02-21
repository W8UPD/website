from django.db import models

class UserProfile(models.Model):
    license_class = models.CharField(max_length=255)
    office = models.CharField(max_length=3, choice=OFFICE_CHOICES) # why 3 characters to define the class....wtf? WLet me show you how I did it last time.
