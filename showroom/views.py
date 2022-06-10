from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import Car, CarManufacturer, Customer, User, Supplier, Showroom
from showroom.serializers import CarListSerializer, CarManufacturerSerializer, CustomerSerializer,  \
    SupplierListRetrieveSerializer, ShowroomListRetrieveSerializer
from .service import CarFilter


class CarViewSet(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CarFilter


class CarManufacturerViewSet(mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.RetrieveModelMixin,
                             viewsets.GenericViewSet):
    serializer_class = CarManufacturerSerializer
    queryset = CarManufacturer.objects.all()


class CustomerViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


# class UserViewSet(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   mixins.RetrieveModelMixin,
#                   mixins.UpdateModelMixin,
#                   viewsets.GenericViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()


class SupplierViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = SupplierListRetrieveSerializer
    queryset = Supplier.objects.all()


class ShowroomViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = ShowroomListRetrieveSerializer
    queryset = Showroom.objects.all()