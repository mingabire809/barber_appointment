# Generated by Django 3.2.6 on 2022-05-20 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0015_auto_20220520_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='pay_now',
            field=models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], default='NO', max_length=150, null=True, verbose_name='Pay Now'),
        ),
    ]