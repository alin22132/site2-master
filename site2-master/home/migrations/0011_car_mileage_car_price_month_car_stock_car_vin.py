# Generated by Django 4.2.5 on 2023-11-19 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_car_engine_car_fuel_car_gearbox_car_traction'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='mileage',
            field=models.TextField(default='N/A'),
        ),
        migrations.AddField(
            model_name='car',
            name='price_month',
            field=models.CharField(default='N/A', max_length=10),
        ),
        migrations.AddField(
            model_name='car',
            name='stock',
            field=models.TextField(default='N/A'),
        ),
        migrations.AddField(
            model_name='car',
            name='vin',
            field=models.TextField(default='N/A'),
        ),
    ]
