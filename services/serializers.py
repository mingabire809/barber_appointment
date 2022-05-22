from rest_framework import serializers
from .models import HairCut, ExtraService


class HairCutSerializer(serializers.ModelSerializer):
    class Meta:
        model = HairCut
        fields = ['hair_cut_type', 'picture', 'price']


class ExtraServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraService
        fields = ['type_of_service', 'service_picture', 'service_price']
