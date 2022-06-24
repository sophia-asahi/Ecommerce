# Generated by Django 3.2.5 on 2022-05-18 06:28

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0037_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('city', models.CharField(blank=True, default='', max_length=50)),
                ('country', models.CharField(blank=True, default='', max_length=50)),
                ('address', models.CharField(blank=True, default='', max_length=50)),
                ('phone', models.CharField(blank=True, default='', max_length=50)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce_app.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce_app.product')),
            ],
        ),
    ]
