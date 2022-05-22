from django.db import models
from member.models import Member
from premium.models import Premium
from membership.models import Membership
from booking.models import Booking
import random
import string
from datetime import date
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.

class Payment(models.Model):

    def transaction(format=None):
        upper = string.ascii_uppercase
        num1 = string.digits
        num2 = string.digits
        num3 = string.digits
        all = upper + num1 + num2 + num3
        temp = random.sample(all, 20)
        transaction = "".join(temp)
        return transaction

    PAYMENT_METHOD = [('PREMIUM', 'Premium'),
                      ('M-PESA', 'M-Pesa'),
                      ('VISA CARD', 'Visa Card'),
                      ('MASTERCARD', 'MasterCard'),
                      ('CASH', 'Cash')]

    transaction_number = models.CharField(unique=True, primary_key=True, verbose_name='Transaction Number',
                                          max_length=30, default=transaction)
    transaction_date = models.DateField(auto_now=True, verbose_name='Transaction date')
    member = models.ForeignKey(Member, verbose_name='User', null=True, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Name', max_length=150, null=True)
    email = models.CharField(verbose_name='Email', max_length=150, null=True)
    phone = models.BigIntegerField(verbose_name='Phone Number', null=True)
    payment_method = models.CharField(verbose_name='Payment method', max_length=50, choices=PAYMENT_METHOD)
    booking_reference_number = models.ForeignKey(Booking, verbose_name='booking reference number', null=True,
                                                 on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, verbose_name='Total to pay')
    premium_reference_number = models.ForeignKey(Premium, verbose_name='Premium Number', null=True,
                                                 on_delete=models.CASCADE)
    balance = models.DecimalField(verbose_name='Premium balance', max_digits=6, decimal_places=2, blank=True)
    coupon = models.DecimalField(max_digits=2, decimal_places=2, verbose_name='Premium coupon discount', null=True)
    premium_expiration = models.DateField(verbose_name='Premium expiry date', blank=True)

    def save(self, *args, **kwargs):
        #  if Premium.balance < Booking.total_price:
        #     raise ValueError('Insufficient balance')

        # if self.premium_reference_number.isExpired:
        #     raise ValueError('Premium expired!')
        # if self.booking_reference_number.total_price > self.premium_reference_number.balance:
        #     raise ValueError('Insufficient balance')

        if not self.total_price:
            self.total_price = self.booking_reference_number.total_price
        if not self.balance:
            self.balance = self.premium_reference_number.balance
        if not self.coupon:
            self.coupon = self.premium_reference_number.coupon
        if not self.premium_expiration:
            self.premium_expiration = self.premium_reference_number.expiry_date

        balance = self.premium_reference_number
        balance.balance = balance.balance - (self.total_price - (self.total_price * self.coupon))
        booking = self.booking_reference_number
        booking.paid = True
        balance.save()
        booking.save()

        super(Payment, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.transaction_number}, {self.transaction_date}, {self.member}, {self.name}, {self.email}, {self.phone}, {self.payment_method}, {self.booking_reference_number}, {self.total_price}, {self.premium_reference_number}, {self.balance}, {self.premium_expiration}'


@receiver(pre_save, sender=Payment, dispatch_uid='Update premium balance')
def update_balance(sender, **kwargs):
    payment = kwargs['instance']
    if payment.pk:
        Premium.objects.filter(pk=payment.premium_reference_number).update(
            balance=payment.balance - (payment.total_price - (payment.total_price * payment.coupon)))
