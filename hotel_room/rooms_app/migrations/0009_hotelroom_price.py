# Generated by Django 4.2.5 on 2023-10-20 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms_app', '0008_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelroom',
            name='price',
            field=models.IntegerField(default=5000, max_length=30),
        ),
    ]
