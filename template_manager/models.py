from django.db import models
from django.core.files.storage import FileSystemStorage


fs = FileSystemStorage(location='templates/CV_Templates')
css_storage =  FileSystemStorage(location='static/css/templates')
class Template(models.Model):
    name = models.CharField(
        max_length=20,
    )
    image = models.ImageField(
        upload_to = 'img/templates/',
        null = True,
        blank = False,
    )
    file = models.FileField(
        storage=fs,
    )
    css_file = models.FileField(
        storage=css_storage,
        null=True,
    )