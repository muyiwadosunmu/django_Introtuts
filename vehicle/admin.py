from django.contrib import admin
from .models import Brand, Location, Feature, VehicleModel, Vehicle, Image

# Register your models here.
admin.site.register((Brand, Location, Feature, VehicleModel, Vehicle, Image))
