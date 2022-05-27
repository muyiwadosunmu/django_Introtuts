from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
vehicle_types = (
    "Sedan",
    "Coupe",
    "Sport Car",
    "Station Wagon",
    "Hatchback",
    "Convertible",
    "SUV",
    "Minivan",
    "Pickup"
)

gear_types = (
    "Manual",
    "Automatic"
)

vehicle_conditions = (
    "Brand New",
    "Locally Used",
    "Foreign Used"
)


class Location(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    class Meta:
        unique_together = ('city', 'state', 'country')

    def __str__(self):
        return f"{self.city} - {self.state} - {self.country}"


class DateControl(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Brand(DateControl):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class VehicleModel(DateControl):
    brand = models.ForeignKey(Brand, related_name="models", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('brand', 'name')

    def __str__(self):
        return self.name


class Feature(DateControl):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Vehicle(DateControl):
    added_by = models.ForeignKey(User, related_name="user_vehicles", on_delete=models.CASCADE)
    model = models.ForeignKey(VehicleModel, related_name="vehicles", on_delete=models.CASCADE)
    common_name = models.CharField(max_length=150)
    vehicle_type = models.CharField(max_length=20, choices=((i, i) for i in vehicle_types))
    gear_type = models.CharField(max_length=15, choices=((i, i) for i in gear_types))
    condition = models.CharField(max_length=15, choices=((i, i) for i in vehicle_conditions))
    year = models.PositiveIntegerField()
    location = models.ForeignKey(Location, related_name="vehicles", on_delete=models.CASCADE)
    mileage = models.FloatField()
    price = models.FloatField()
    slug = models.CharField(max_length=150, null=True)
    negotiable = models.BooleanField()
    features = models.ManyToManyField(Feature, related_name="vehicle_features")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.common_name)
        #save the location First
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.common_name} - {self.created_at}"


class Image(DateControl):
    vehicle = models.ForeignKey(Vehicle, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="car_images")

    def __str__(self):
        return f"{self.vehicle.common_name} - {self.vehicle.created_at}"

