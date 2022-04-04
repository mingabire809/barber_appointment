# Generated by Django 3.2.6 on 2022-03-13 13:26

import booking.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0003_auto_20220309_0935'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_reference_number', models.CharField(default=booking.models.Booking.reference, max_length=30, unique=True, verbose_name='Booking number')),
                ('booking_username', models.CharField(blank=True, max_length=150)),
                ('booking_user_email', models.CharField(blank=True, max_length=150)),
                ('base_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('extra_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('booking_date', models.DateTimeField(auto_now_add=True, verbose_name='Time')),
                ('is_processed', models.BooleanField(default=False)),
                ('booking_user', models.ForeignKey(blank=True, max_length=150, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('extra_services', models.ForeignKey(max_length=150, on_delete=django.db.models.deletion.CASCADE, to='services.extraservice', verbose_name='Extra Service')),
                ('hair_cut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.haircut', verbose_name='Hair Cut')),
            ],
        ),
    ]
