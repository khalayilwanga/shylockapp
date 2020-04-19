from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.


class CustomUserManager(UserManager):
    def get_by_natural_key(self, email):
        return self.get(email=email)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(default="Your name", max_length=70)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
