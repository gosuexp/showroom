from django.db import models
from django.contrib.auth.models import PermissionsMixin, User
from django_countries.fields import CountryField



#car
class CarManufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    CAR_TYPE_CHOICES = [
        ('Sedan', 'Sedan'),
        ('Coupe', 'Coupe'),
        ('Crossover', 'Crossover'),
        ('HatchBack', 'HatchBack')
    ]
    manufacturer = models.ForeignKey(CarManufacturer, on_delete=models.CASCADE)
    car_type = models.CharField(max_length=100, choices=CAR_TYPE_CHOICES)
    model = models.CharField(max_length=100, unique=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.manufacturer}{self.model}'


#customer
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField()
    email = models.EmailField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user


class CustomerHistory(models.Model):
    name = models.CharField(max_length=100)
    start_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField()
    percent = models.DecimalField(decimal_places=2, max_digits=4)
    cars = models.ManyToManyField('Car')
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    showroom = models.ForeignKey('Showroom', on_delete=models.CASCADE)

    def __str__(self):
        return (self.name)


class Showroom(models.Model):
    name = models.CharField(max_length=80)
    location = CountryField()
    balance = models.DecimalField(decimal_places=2, max_digits=5)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    cars = models.ManyToManyField('Car', blank=True)
    customers = models.ManyToManyField('Customer', blank=True)

    def __str__(self):
        return self.name


class ShowroomDiscount(models.Model):
    showroom = models.ForeignKey('Showroom', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField()
    percent = models.DecimalField(decimal_places=2, max_digits=4)
    cars = models.ManyToManyField('Car')

    def __str__(self):
        return self.showroom


class ShowroomHistory(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    showroom = models.ForeignKey('Showroom', on_delete=models.CASCADE)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)


#supplier(postavshik)
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    foundation_year = models.DateField()
    cars = models.ManyToManyField('Car', blank=True)
    showrooms = models.ManyToManyField('Showroom', blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SupplierDiscount(models.Model):
    name = models.CharField(max_length=100)
    start_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField()
    percent = models.DecimalField(decimal_places=2, max_digits=4)
    cars = models.ManyToManyField('Car')
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)

    def __str__(self):
        return self.name