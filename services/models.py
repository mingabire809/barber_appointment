from django.db import models


# Create your models here.

class HairCut(models.Model):
    hair_cut_type = models.CharField(primary_key=True, max_length=150, verbose_name='Type of Haircut')
    picture = models.ImageField(upload_to='Haircut', verbose_name='Image of haircut')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='price')

    def __str__(self):
        return f'{self.hair_cut_type}, {self.picture}, {self.price}$'


class ExtraService(models.Model):
    type_of_service = models.CharField(primary_key=True, max_length=150, verbose_name='Available extra Service')
    service_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='price')
    service_picture = models.ImageField(upload_to='services', verbose_name='Image of services', null=True)

    def __str__(self):
        return f'{self.type_of_service}, {self.service_picture}, {self.service_price}$'
