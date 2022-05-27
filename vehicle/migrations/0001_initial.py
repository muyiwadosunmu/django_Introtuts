# Generated by Django 4.0.4 on 2022-05-26 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
            options={
                'unique_together': {('city', 'state', 'country')},
            },
        ),
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='vehicle.brand')),
            ],
            options={
                'unique_together': {('brand', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('common_name', models.CharField(max_length=150)),
                ('vehicle_type', models.CharField(choices=[('Sedan', 'Sedan'), ('Coupe', 'Coupe'), ('Sport Car', 'Sport Car'), ('Station Wagon', 'Station Wagon'), ('Hatchback', 'Hatchback'), ('Convertible', 'Convertible'), ('SUV', 'SUV'), ('Minivan', 'Minivan'), ('Pickup', 'Pickup')], max_length=20)),
                ('gear_type', models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], max_length=15)),
                ('condition', models.CharField(choices=[('Brand New', 'Brand New'), ('Locally Used', 'Locally Used'), ('Foreign Used', 'Foreign Used')], max_length=15)),
                ('year', models.PositiveIntegerField()),
                ('mileage', models.FloatField()),
                ('price', models.FloatField()),
                ('negotiable', models.BooleanField()),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_vehicles', to=settings.AUTH_USER_MODEL)),
                ('features', models.ManyToManyField(related_name='vehicle_features', to='vehicle.feature')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='vehicle.location')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='vehicle.vehiclemodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='car_images')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='vehicle.vehicle')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
