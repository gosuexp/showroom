from rest_framework import mixins, viewsets
from .models import Car, CarManufacturer, Customer
from showroom.serializers import CarListSerializer, CarManufacturerSerializer, CustomerSerializer


class CarViewSet(
            mixins.ListModelMixin,
            mixins.CreateModelMixin,
            mixins.UpdateModelMixin,
            mixins.RetrieveModelMixin,
            viewsets.GenericViewSet):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer


class CarManufacturerViewSet(
                mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.RetrieveModelMixin,
                viewsets.GenericViewSet, ):
    serializer_class = CarManufacturerSerializer
    queryset = CarManufacturer.objects.all()


class CustomerViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

