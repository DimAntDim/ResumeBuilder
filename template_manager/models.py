from django.db import models
from django.core.files.storage import FileSystemStorage


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