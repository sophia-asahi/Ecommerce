# Generated by Django 3.2.5 on 2022-05-16 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0019_order_uuidmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='UUIDModel',
        ),
    ]
