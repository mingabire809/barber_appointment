# Generated by Django 3.2.6 on 2022-05-19 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Membership')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='price')),
            ],
        ),
    ]
