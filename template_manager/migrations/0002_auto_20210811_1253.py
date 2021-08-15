# Generated by Django 3.2.6 on 2021-08-11 09:53

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('template_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='image',
            field=models.ImageField(null=True, upload_to='img/templates/'),
        ),
        migrations.AlterField(
            model_name='template',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='templates/CV_Templates'), upload_to=''),
        ),
    ]
