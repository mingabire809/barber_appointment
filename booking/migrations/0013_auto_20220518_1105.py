# Generated by Django 3.2.6 on 2022-05-18 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_auto_20220420_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='base_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='booking',
            name='extra_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
