# Generated by Django 4.2.5 on 2023-10-19 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms_app', '0006_reservation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]
