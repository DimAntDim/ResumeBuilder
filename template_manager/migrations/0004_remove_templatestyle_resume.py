# Generated by Django 3.2.6 on 2021-11-02 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('template_manager', '0003_auto_20211102_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='templatestyle',
            name='resume',
        ),
    ]
