# Generated by Django 3.2.6 on 2022-03-14 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20220314_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='phonenumber',
        ),
    ]
