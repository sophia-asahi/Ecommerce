# Generated by Django 3.2.5 on 2022-05-16 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0022_remove_order_order_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]