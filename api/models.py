
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # additional fields here
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='users/', null=True, blank=True)

    def __str__(self):
        return self.username