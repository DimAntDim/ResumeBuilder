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

    def __srt__(self):
        return self.name


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
    name = models.CharField(
        max_length=60,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

class Education(models.Model):
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

class EmploymentHistory(models.Model):
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
    description = models.TextField()

    def __str__(self):
        return f"Company: {self.company_name}\nRole: {self.role}\nStart date: {self.start}\nEnd date: {self.end}\nDesctiption: {self.description}"

class Languages(models.Model):
    
    language = models.CharField(
        max_length=60,
        null=True,
        blank=True,
    )
    def __str__(self):
        return self.language


class Resume(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        default='',
        )
    personal_info = models.ForeignKey(
        PersonalInfo,
        on_delete=models.CASCADE,
        null=True,
    )
    skills = models.ForeignKey(
        Skills,
        on_delete=models.CASCADE,
        null=True,
    )
    education = models.ForeignKey(
        Education,
        on_delete=models.CASCADE,
        null=True,
    )
    employment_history = models.ForeignKey(
        EmploymentHistory,
        on_delete=models.CASCADE,
        null=True,
    )
    languages = models.ForeignKey(
        Languages,
        on_delete=models.CASCADE,
        null=True,
    )