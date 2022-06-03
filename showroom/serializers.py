from rest_framework import serializers
from .models import *


class CarListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'


class CarManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarManufacturer
        fields = ('name',)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
