from main.celery import app
from .models import CustomerOrder, CustomerHistory, Showroom, Supplier, ShowroomHistory


@app.task
def customers_buy_cars():
    x = []
    for order in CustomerOrder.objects.all():
        for showroom in Showroom.objects.all():
            for y in showroom.cars.all():
                x.append(y.manufacturer)
                if order.manufacturer in x and y.price <= order.price:
                    CustomerHistory.objects.create(manufacturer=order.manufacturer,
                                                   customer=order.customer,
                                                   showroom=Showroom.objects.all()[0],
                                                   price=y.price)
                    ShowroomHistory.objects.create(manufacturer=order.manufacturer,
                                                   showroom=Showroom.objects.all()[0],
                                                   price=order.price)


@app.task
def showroom_buy_car():
    for showroom in Showroom.objects.all():
        for supplier in Supplier.objects.all():
            for car in supplier.cars.all():
                showroom.cars.add(car)
                showroom.save()
