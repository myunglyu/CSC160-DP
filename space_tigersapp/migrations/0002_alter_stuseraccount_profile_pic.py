# Generated by Django 5.1.2 on 2024-10-15 04:21

import space_tigersapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space_tigersapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuseraccount',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=space_tigersapp.models.PathAndRename('profile_pictures/'), verbose_name='Profile Picture'),
        ),
    ]
