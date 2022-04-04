import random
import string

import requests
from django.contrib.auth import get_user
from django.contrib.auth.models import User, AbstractUser
from django.db import models
# from rest_framework import request
# from django.http import request


from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication, BasicAuthentication

from member.models import Member
from services.models import HairCut, ExtraService


# Create your models here.

class Booking(models.Model):
    #   def sample_view(self, request, format=None):
    #       current_user = request.user
    #       print(current_user.id)
    #       return current_user.username

    #   def sample_email(self, request, format=None):
    #       current_user = request.user
    #       print(current_user.id)
    #       return current_user.email

    #   def sample_fullname(self, request, format=None):
    #       current_user = request.user
    #       print(current_user.id)
    #       return current_user.full_name

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def my_view_username(self, request, format=None):
        username = None
        if request.user.is_authenticated():
            username = request.user.username
            return username
        return username

    def my_view_fullname(self, request, format=None):
        full_name = None
        if request.user.is_authenticated():
            full_name = request.user.full_name
            return full_name

    def my_view_email(self, request, format=None):
        email = None
        if request.user.is_authenticated():
            email = request.user.email
            return email

    def reference(format=None):
        upper = string.ascii_uppercase
        num = string.digits
        all = upper + num
        temp = random.sample(all, 20)
        reference = "".join(temp)
        return reference

    booking_reference_number = models.CharField(unique=True, verbose_name='Booking number', default=reference,
                                                max_length=30)
    # booking_person = models.ForeignKey(Member, verbose_name='Member', on_delete=models.CASCADE)
    # booking_user = models.ForeignKey(Member,  Member.full_name, on_delete=models.CASCADE, verbose_name="Member name")
    # full_name = models.CharField(blank=True, max_length=150)
    # booking_username = Member.objects.get(username=booking_person.member.username)
    # booking_username = models.CharField(max_length=150, blank=True)
    # email = models.CharField(max_length=150, blank=True)
    #  customer = models.ForeignKey(Member, verbose_name='customer', on_delete=models.CASCADE, null=True)
    member = models.ForeignKey(Member, verbose_name='customer', null=True, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Customer name',  max_length=150, null=True)
    email = models.CharField(verbose_name='Customer email', max_length=150, null=True)
    phone = models.BigIntegerField(verbose_name='Customer Phone Number', null=True)
    hair_cut = models.ForeignKey(HairCut, verbose_name='Hair Cut', on_delete=models.CASCADE)
    extra_services = models.ForeignKey(ExtraService, verbose_name='Extra Service', max_length=150,
                                       on_delete=models.CASCADE)
    base_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    extra_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    # total_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    booking_date = models.DateTimeField(auto_now_add=True, verbose_name='Time')
    is_processed = models.BooleanField(default=False)

    # first_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='hair cut price', default=base_price)
    # second_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='service price', default=extra_price)

    def save(self, *args, **kwargs):
        if not self.base_price:
            self.base_price = self.hair_cut.price
        if not self.extra_price:
            self.extra_price = self.extra_services.service_price
        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.booking_reference_number} ,{self.booking_date}, {self.hair_cut}, {self.extra_services}, {self.base_price}$, {self.extra_price}$'
