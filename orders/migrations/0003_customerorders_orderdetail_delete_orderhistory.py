# Generated by Django 5.1.2 on 2024-10-16 20:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_initial'),
        ('space_tigersapp', '0002_alter_stuseraccount_profile_pic'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerOrders',
            fields=[
                ('OrderNumber', models.AutoField(primary_key=True, serialize=False, verbose_name='Order Number')),
                ('OrderDate', models.TimeField(verbose_name='Date Ordered')),
                ('Customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qty', models.IntegerField(null=True, verbose_name='Stock Qty')),
                ('ShippingAddress', models.TextField(verbose_name='Shipping Address')),
                ('OrderNumber', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.customerorders')),
                ('ProductID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='space_tigersapp.product')),
            ],
        ),
        migrations.DeleteModel(
            name='OrderHistory',
        ),
    ]
