# Generated by Django 5.0.6 on 2024-07-05 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_brand_alter_car_value_alter_car_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='plate',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
