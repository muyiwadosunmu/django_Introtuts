from django.db import models
from django.utils.text import slugify

from vehicle.models import Location, User, DateControl

# Create your models here.

user_types = (
    "Dealer",
    "Personal",
    "Organization"
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="user_profile", on_delete=models.CASCADE)
    phone_number = models.PositiveBigIntegerField()
    user_type = models.CharField(max_length=20, choices=((i, i) for i in user_types))
    location = models.ForeignKey(Location, related_name="users", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        # save the location First

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.email}"
