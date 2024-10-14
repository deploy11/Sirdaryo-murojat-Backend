from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
     organization = models.CharField(max_length=255, blank=True, null=True)