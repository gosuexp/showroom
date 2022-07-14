from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from core.enums.car import CarType
from core.models import abstract_models


#car
class CarManufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Car(abstract_models.Abstract):
    manufacturer = models.ForeignKey(CarManufacturer, on_delete=models.CASCADE)
    car_type = models.CharField(max_length=100, verbose_name="Car Type", choices=CarType.choices())
    model = models.CharField(max_length=100, unique=True, verbose_name="Model")
    price = models.IntegerField(default=10000, verbose_name="Car price")

    def __str__(self):
        return str(self.manufacturer)

    class Meta:
        verbose_name = "Car model"
        verbose_name_plural = "Car models"
        ordering = ['-created_at', 'car_type']


#customer
class Customer(abstract_models.Abstract):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Customer name")
    balance = models.IntegerField(null=True, verbose_name="Customer balance")
    email = models.EmailField(max_length=200, null=True, verbose_name="Customer email")

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['-created_at', 'user']


class CustomerHistory(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=10)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    showroom = models.ForeignKey('Showroom', on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(CarManufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.manufacturer}-{self.price}'


class CustomerOrder(models.Model):
    manufacturer = models.ForeignKey(CarManufacturer, on_delete=models.CASCADE)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.manufacturer}-{self.price}'


#showroom
class Showroom(abstract_models.Abstract):
    name = models.CharField(max_length=80, verbose_name='Showroom name')
    location = CountryField(verbose_name="Location")
    balance = models.DecimalField(decimal_places=2, max_digits=10,null=True, verbose_name="Showroom balance")
    cars = models.ManyToManyField('Car', blank=True)
    customers = models.ManyToManyField('Customer', blank=True)

    def __str__(self):
        return f'{self.name},{self.cars}'

    class Meta:
        verbose_name = 'Showroom'
        verbose_name_plural = 'Showrooms'
        ordering = ['-created_at', 'name']


class ShowroomHistory(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=10)
    showroom = models.ForeignKey('Showroom', on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(CarManufacturer, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.manufacturer},{self.price}'


#supplier
class Supplier(abstract_models.Abstract):
    name = models.CharField(max_length=100, verbose_name="Supplier name")
    foundation_year = models.DateField(verbose_name="Year of foundation")
    cars = models.ManyToManyField('Car', blank=True)
    showrooms = models.ManyToManyField('Showroom', blank=True)
    location = CountryField(blank=True)

    def __str__(self):
        return f'{self.name} - {self.cars}'

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
        ordering = ['-created_at', 'name']