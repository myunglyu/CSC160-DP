# Generated by Django 5.1.2 on 2024-10-17 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_customerorders_orderdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorders',
            name='ItemsOrdered',
            field=models.JSONField(default=[], verbose_name='ItemsOrdered'),
        ),
        migrations.DeleteModel(
            name='OrderDetail',
        ),
    ]
