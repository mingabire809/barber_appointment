from rest_framework import serializers
from .models import Booking
from member.models import Member


# class BookingMember(serializers.ModelSerializer):
#    class Meta:
#        model = Member
#        fields = ['full_name', 'email', 'phone_number', 'id']


class BookingSerializer(serializers.ModelSerializer):
    #   customer = BookingMember(required=False)

    #   def _user(self, obj):
    #       request = self.context.get('request', None)
    #       if request:
    #           return request.user.full_name

    #  def _email(self, obj):
    #      request = self.context.get('request', None)
    #      if request:
    #          return request.user.email

    #  def _phone(self, obj):
    #      request = self.context.get('request', None)
    #      if request:
    #          return request.user.phone_number

    class Meta:
        model = Booking
        fields = ('booking_reference_number', 'member', 'name', 'email', 'phone', 'hair_cut',
                  'extra_services',
                  'base_price', 'extra_price', 'booking_date', 'is_processed')

    def create(self, validated_data):
        # account_data = validated_data.pop('customer')
        # account = Member(**account_data)
        # account.set_password(account.password)
        # account.save()
        return Booking.objects.create(**validated_data)
