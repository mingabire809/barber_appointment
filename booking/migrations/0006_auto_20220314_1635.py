# Generated by Django 3.2.6 on 2022-03-14 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_remove_booking_phonenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='email',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='full_name',
        ),
    ]