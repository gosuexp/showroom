# Generated by Django 4.0.4 on 2022-06-03 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_type', models.CharField(choices=[('Sedan', 'Sedan'), ('Coupe', 'Coupe'), ('Crossover', 'Crossover'), ('HatchBack', 'HatchBack')], max_length=100)),
                ('model', models.CharField(max_length=100, unique=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarManufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('email', models.EmailField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Showroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('location', django_countries.fields.CountryField(max_length=2)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=5)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('cars', models.ManyToManyField(blank=True, to='showroom.car')),
                ('customers', models.ManyToManyField(blank=True, to='showroom.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('foundation_year', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cars', models.ManyToManyField(blank=True, to='showroom.car')),
                ('showrooms', models.ManyToManyField(blank=True, to='showroom.showroom')),
            ],
        ),
        migrations.CreateModel(
            name='SupplierDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_at', models.DateTimeField(auto_now_add=True)),
                ('end_at', models.DateTimeField()),
                ('percent', models.DecimalField(decimal_places=2, max_digits=4)),
                ('cars', models.ManyToManyField(to='showroom.car')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showroom.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='ShowroomHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showroom.car')),
                ('showroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showroom.showroom')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showroom.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='ShowroomDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_at', models.DateTimeField(auto_now_add=True)),
                ('end_at', models.DateTimeField()),
                ('percent', models.DecimalField(decimal_places=2, max_digits=4)),
                ('cars', models.ManyToManyField(to='showroom.car')),
                ('showroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showroom.showroom')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_at', models.DateTimeField(auto_now_add=True)),
                ('end_at', models.DateTimeField()),
                ('percent', models.DecimalField(decimal_places=2, max_digits=4)),
                ('cars', models.ManyToManyField(to='showroom.car')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showroom.customer')),
                ('showroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showroom.showroom')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showroom.carmanufacturer'),
        ),
    ]
