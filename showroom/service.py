from .models import Car
from django_filters import rest_framework as filters


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
   pass


class CarFilter(filters.FilterSet):

    class Meta:
        model = Car
        fields = ['manufacturer', 'car_type', 'model']



