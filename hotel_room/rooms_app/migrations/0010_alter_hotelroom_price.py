# Generated by Django 4.2.5 on 2023-10-27 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms_app', '0009_hotelroom_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelroom',
            name='price',
            field=models.IntegerField(default=5000),
        ),
    ]
