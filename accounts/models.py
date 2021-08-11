from account_auth.models import CustomUser
from django.db import models

class Profile(models.Model):
    first_name = models.CharField(
        max_length=20,
        blank=False,
        null=True,
    )
    last_name = models.CharField(
        max_length=20,
        blank=False,
        null=True,
    ) 
    profile_image = models.ImageField(
        upload_to = 'profiles/images/',
        blank=True,
    )
    user = models.OneToOneField(
        CustomUser, 
        on_delete=models.CASCADE,
        primary_key=True,
        )
    is_complete = models.BooleanField(
        default=False,
    )
    class Meta:
        verbose_name_plural = ("Profiles")

    def __str__(self):
        return self.user.email


from account_auth.signals import *