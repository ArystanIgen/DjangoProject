# Generated by Django 3.1.7 on 2021-05-16 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cartitem_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='customer',
        ),
    ]
