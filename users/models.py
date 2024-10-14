from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    type = models.CharField(max_length=500,null=True,blank=True)
    tashkilot = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return f"{self.username} - {self.type}"
