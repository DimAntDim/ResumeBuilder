# Generated by Django 3.2.6 on 2021-08-15 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('template_manager', '0005_remove_template_user'),
        ('accounts', '0002_templates'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Templates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('occupation', models.CharField(max_length=30, null=True)),
                ('address', models.CharField(max_length=20, null=True)),
                ('city', models.CharField(max_length=20, null=True)),
                ('country', models.CharField(max_length=20, null=True)),
                ('phone', models.IntegerField()),
                ('about_me', models.TextField()),
                ('employment_history', models.TextField()),
                ('education', models.TextField()),
                ('skills', models.TextField()),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='template_manager.template')),
            ],
        ),
        migrations.DeleteModel(
            name='Templates',
        ),
    ]
