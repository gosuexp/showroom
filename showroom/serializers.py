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
        read_only_fields = ('balance',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class SupplierListRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('name', 'foundation_year', 'cars', 'showrooms')


class ShowroomListRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroom
        exclude = ('time_create', 'time_update')
        read_only_fields = ('balance',)