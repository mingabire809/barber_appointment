from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['transaction_number', 'transaction_date', 'member',
                  'name', 'email', 'phone', 'payment_method', 'booking_reference_number',
                  'total_price', 'premium_reference_number', 'balance', 'coupon', 'premium_expiration']

    def create(self, validated_data):
        # account_data = validated_data.pop('customer')
        # account = Member(**account_data)
        # account.set_password(account.password)
        # account.save()
        return Payment.objects.create(**validated_data)
