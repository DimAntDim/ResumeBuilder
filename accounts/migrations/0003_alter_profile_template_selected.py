# Generated by Django 3.2.6 on 2021-08-19 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_template_selected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='template_selected',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
