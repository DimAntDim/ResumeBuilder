from template_manager.models import Template
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

class User_Templates(models.Model):
    template = models.ForeignKey(
        Template,
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(
        max_length=20,
        null=True,
    )
    last_name =models.CharField(
        max_length=20,
        null=True,
    )
    occupation = models.CharField(
        max_length=30,
        null=True,
    )
    address = models.CharField(
        max_length=20,
        null=True,
    )
    city = models.CharField(
        max_length=20,
        null=True,
    )
    country = models.CharField(
        max_length=20,
        null=True,
    )
    phone = models.IntegerField()
    contact_email = models.EmailField
    about_me = models.TextField()
    employment_history = models.TextField()
    education = models.TextField()
    skills = models.TextField()


from account_auth.signals import *