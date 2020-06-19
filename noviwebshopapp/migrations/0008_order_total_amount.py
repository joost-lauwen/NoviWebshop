# Generated by Django 3.0.3 on 2020-06-19 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noviwebshopapp', '0007_order_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9999),
        ),
    ]