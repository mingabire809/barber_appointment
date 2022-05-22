from django.db import models


# Create your models here.

class Membership(models.Model):
    name = models.CharField(primary_key=True, verbose_name='Membership', max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='price')
    discount = models.DecimalField(max_digits=2, decimal_places=2, verbose_name='Membership discount', null=True)
    duration = models.IntegerField(verbose_name='Membership duration', null=True)

    def __str__(self):
        return f'{self.name}, {self.price}$, {self.discount}, {self.duration} months'
