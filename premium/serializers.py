from rest_framework import serializers
from .models import Premium


class PremiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Premium
        fields = ['premium_reference_number', 'member',
                  'name', 'email', 'phone', 'membership', 'price',
                  'date', 'expiry_date', 'balance', 'coupon', 'isExpired']

    def create(self, validated_data):
        # account_data = validated_data.pop('customer')
        # account = Member(**account_data)
        # account.set_password(account.password)
        # account.save()
        return Premium.objects.create(**validated_data)
