# Generated by Django 3.2.6 on 2021-11-02 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile_number_of_saved_resumes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='number_of_saved_resumes',
        ),
    ]
