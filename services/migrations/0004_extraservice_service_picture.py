# Generated by Django 3.2.6 on 2022-04-05 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20220309_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='extraservice',
            name='service_picture',
            field=models.ImageField(null=True, upload_to='services', verbose_name='Image of services'),
        ),
    ]
