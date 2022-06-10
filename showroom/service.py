from .models import Car
from django_filters import rest_framework as filters


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
   pass


class CarFilter(filters.FilterSet):
    car_type = CharFilterInFilter(field_name='car_type', lookup_expr='in')
    price = filters.RangeFilter(field_name='price')

    class Meta:
        model = Car
        fields = ['manufacturer', 'car_type', 'model']



