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

    IMMEDIATE_PAYMENT = [('YES', 'Yes'),
                         ('NO', 'No')]
    PAYMENT_METHOD = [('PREMIUM', 'Premium'),
                      ('M-PESA', 'M-Pesa'),
                      ('VISA CARD', 'Visa Card'),
                      ('MASTERCARD', 'MasterCard'),
                      ('CASH', 'Cash')]
    PLACE = [('HOME', 'Home'),
             ('ON-SITE', 'On-site')]

    booking_reference_number = models.CharField(verbose_name='Booking number', default=reference,
                                                max_length=30, primary_key=True)
    member = models.ForeignKey(Member, verbose_name='customer', null=True, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Customer name', max_length=150, null=True)
    email = models.CharField(verbose_name='Customer email', max_length=150, null=True)
    phone = models.BigIntegerField(verbose_name='Customer Phone Number', null=True)
    hair_cut = models.ForeignKey(HairCut, verbose_name='Hair Cut', on_delete=models.CASCADE)
    extra_services = models.ForeignKey(ExtraService, verbose_name='Extra Service', max_length=150,
                                       on_delete=models.CASCADE, null=True)
    location = models.CharField(max_length=20, verbose_name='Place', blank=True, null=True)
    base_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0.0)
    extra_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0.0)
    total_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0.0)
    pay_now = models.CharField(verbose_name='Pay Now', max_length=150, blank=True,
                               choices=IMMEDIATE_PAYMENT, null=True, default='NO')
    payment_method = models.CharField(verbose_name='Method of Payment', max_length=150, blank=True, null=True,
                                      choices=PAYMENT_METHOD)
    booking_date = models.DateTimeField(auto_now_add=True, verbose_name='Time')
    paid = models.BooleanField(verbose_name='Paid', default=False)
    is_processed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.base_price:
            self.base_price = self.hair_cut.price
        if not self.extra_price:
            self.extra_price = self.extra_services.service_price
        if not self.total_price:
            self.total_price = self.base_price + self.extra_price
        if self.location == 'HOME':
            self.total_price = self.base_price + self.extra_price + 6.99
        if self.pay_now == 'NO':
            self.payment_method = 'CASH'

        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.booking_reference_number} ,{self.booking_date}, {self.hair_cut}, {self.extra_services}, {self.location},{self.base_price}$, {self.extra_price}$, {self.total_price}$, {self.pay_now}, {self.payment_method}, {self.booking_date}, {self.paid}'
