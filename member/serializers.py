from .models import Member
from rest_framework import serializers, request


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['full_name', 'email', 'username', 'phone_number', 'profile_picture', 'password', 'id','is_barber']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        #serializer = MemberSerializer(data=request.data)
        #if serializer.is_valid():
        #    serializer.save()
        return Member.objects.create_user(**validated_data)
