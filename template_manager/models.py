from django.contrib.auth import get_user_model
from django.db import models
from django.core.files.storage import FileSystemStorage

CustomUser = get_user_model()
css_storage =  FileSystemStorage(location='static/css/cv_templates')


class Resume(models.Model):
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
        blank=True,
    )
    last_name =models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    address = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    city = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    country = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    phone = models.IntegerField()
    contact_email = models.EmailField(
        null=True,
    )
    about_me = models.TextField(
        blank=True,
    )

class TemplateStyle(models.Model):
    image = models.ImageField(
        upload_to = 'img/cv_templates/',
        null = True,
        blank = False,
    )
    css_file = models.FileField(
        storage=css_storage,
        null=True,
    )

    def __srt__(self):
        return self.name



class Skills(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        null=True,
    )
    name = models.CharField(
        max_length=60,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

class Education(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        null=True,
    )
    school_name = models.CharField(
        max_length=60,
        null=True,
        blank=True,
    )
    degree = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    start = models.DateField(
        null=True,
        blank=True,
    )
    end = models.DateField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"School: {self.school_name}\nDegree: {self.degree}\nStart date: {self.start}\nEnd date: {self.end}"

class EmploymentHistory(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        null=True,
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
    start = models.DateField(
        null=True,
        blank=True,
    )
    end = models.DateField(
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Company: {self.company_name}\nRole: {self.role}\nStart date: {self.start}\nEnd date: {self.end}\nDesctiption: {self.description}"

class Languages(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        null=True,
    )
    language = models.CharField(
        max_length=60,
        null=True,
        blank=True,
    )
    def __str__(self):
        return self.language
