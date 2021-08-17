from django.db.models.fields.related import ForeignKey
from template_manager.models import TemplateStyle
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
class PersonalInfo(models.Model):
    photo = models.ImageField(
        upload_to = 'profiles/photo/',
        blank=True,
        null=True,
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
class Skills(models.Model):
    name = models.CharField(
        max_length=60,
        null=True,
        blank=True,
    )

class Languages(models.Model):
    language = models.CharField(
        max_length=60,
        null=True,
        blank=True,
    )

class Employment_history(models.Model):
    company_name = models.CharField(
        max_length=60,
        null=True,
        blank=True,
    )
    position = models.CharField(
        max_length=60,
        blank=True,
        null=True,
    )
    start = models.DateField()
    end = models.DateField()
    description = models.TextField(
        blank=True,
    )

class Education(models.Model):
    school_name = models.CharField(
        max_length=60,
        null=True,
    )
    degree = models.CharField(
        max_length=50,
        null=True,
    )
    school_name = models.CharField(
        max_length=60,
        null=True,
        )
    start = models.DateField()
    end = models.DateField()


class User_Templates(models.Model):
    template = models.ForeignKey(
        TemplateStyle,
        on_delete=models.CASCADE,
    )
    employment_history = models.ForeignKey(
        Employment_history,
        on_delete=models.CASCADE,
    )
    education = models.ForeignKey(
        Education,
        on_delete=models.CASCADE,
    )
    skills = models.ForeignKey(
        Skills,
        on_delete=models.CASCADE,
        )
    languages = models.ForeignKey(
        Languages,
        on_delete=models.CASCADE,
    )




from account_auth.signals import *