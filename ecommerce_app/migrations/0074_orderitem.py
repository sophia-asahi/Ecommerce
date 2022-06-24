# Generated by Django 3.2.5 on 2022-06-03 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0073_delete_orderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('price', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('total', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce_app.customer')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce_app.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce_app.product')),
            ],
        ),
    ]
