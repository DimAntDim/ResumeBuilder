# Generated by Django 3.2.6 on 2021-08-18 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('profile_image', models.ImageField(blank=True, upload_to='profiles/images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='account_auth.customuser')),
                ('is_complete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
