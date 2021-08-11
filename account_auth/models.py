from account_auth.managers import CustomUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    
    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __repr__(self):
        return self.type

    class Meta:
        verbose_name_plural = 'Users'

from .signals import *