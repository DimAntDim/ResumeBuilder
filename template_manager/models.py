from django.contrib.auth import get_user_model
from django.db import models
from django.core.files.storage import FileSystemStorage

CustomUser = get_user_model()
css_storage =  FileSystemStorage(location='static/css/cv_templates')
class TemplateStyle(models.Model):
    name = models.CharField(
        max_length=20,
    )
    image = models.ImageField(
        upload_to = 'img/cv_templates/',
        null = True,
        blank = False,
    )
    css_file = models.FileField(
        storage=css_storage,
        null=True,
    )

class PersonalInfo(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        default='',
        )
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
    contact_email = models.EmailField(
        null=True,
    )
    about_me = models.TextField()
class Skills(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        default='',
        )
    name = models.CharField(
        max_length=60,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

class Education(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        default='',
        )

    school_name = models.CharField(
        max_length=60,
        null=True,
    )
    degree = models.CharField(
        max_length=50,
        null=True,
    )
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        
        return f"School: {self.school_name}\nDegree: {self.degree}\nStart date: {self.start}\nEnd date: {self.end}"
class Employment_history(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        default='',
        )
    company_name = models.CharField(
        max_length=60,
        null=True,
        blank=True,
    )
    role = models.CharField(
        max_length=60,
        blank=True,
        null=True,
    )
    start = models.DateField()
    end = models.DateField()
    description = models.TextField(
    )

class Languages(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        default='',
        )
    language = models.CharField(
        max_length=60,
        null=True,
        blank=True,
    )
