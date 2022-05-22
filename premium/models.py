from locale import format_string

from dateutil.relativedelta import relativedelta
from django.db import models
import random
import string
from datetime import date
import datetime
from member.models import Member
from membership.models import Membership



# Create your models here.

class Premium(models.Model):
    def premium_number(format=None):
        upper = string.ascii_uppercase
        num = string.digits
        all = upper + num
        temp = random.sample(all, 10)
        premium_number = "".join(temp)
        return premium_number

    premium_reference_number = models.CharField(verbose_name='Premium number', default=premium_number,
                                                max_length=30, primary_key=True)
    member = models.ForeignKey(Member, verbose_name='Owner', null=True, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Owner name', max_length=150, null=True)
    email = models.CharField(verbose_name='Owner email', max_length=150, null=True)
    phone = models.BigIntegerField(verbose_name='Owner Phone Number', null=True)
    membership = models.ForeignKey(Membership, verbose_name='Membership', null=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    date = models.DateField(auto_now_add=True, verbose_name='Premium Starting Date')
    expiry_date = models.DateField(verbose_name='Premium expiry date', blank=True)
    balance = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='balance', blank=True)
    coupon = models.DecimalField(max_digits=2, decimal_places=2, verbose_name='Premium coupon discount', null=True)
    isExpired = models.BooleanField(verbose_name='premium expired status', default=False)


    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.membership.price
        if not self.balance:
            self.balance = self.price
        if not self.expiry_date:
            # datetime_object = datetime.datetime.strptime(self.date, format_string()).date()
            # new_date = datetime_object + relativedelta(years=1)
            self.expiry_date = date.today() + relativedelta(months=self.membership.duration)
        if not self.coupon:
            self.coupon = self.membership.discount

        super(Premium, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.premium_reference_number}, {self.member}, {self.name}, {self.email}, {self.phone}, {self.membership}, {self.price}$, {self.date}, {self.expiry_date}, {self.balance}, {self.coupon}$,{self.isExpired} '
