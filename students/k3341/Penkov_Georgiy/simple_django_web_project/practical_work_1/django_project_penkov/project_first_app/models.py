from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class Car(models.Model):
    car_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.brand} {self.model} ({self.car_number})"


class CarOwner(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField(blank=True, null=True)
    cars = models.ManyToManyField(Car, through="Ownership")

    passport_number = models.CharField(max_length=10, unique=True)
    home_address = models.CharField(max_length=300, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class DrivingLicence(models.Model):
    LICENSE_TYPES = {
        "A": "Motorcycle",
        "B": "Passenger car",
        "C": "Truck",
    }
    car_owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    license_type = models.CharField(max_length=1, choices=LICENSE_TYPES)
    issue_date = models.DateField()


class Ownership(models.Model):
    car_owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
