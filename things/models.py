
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Thing (models.Model):
    name = models.CharField(unique=True, blank=False, max_length=30)
    description = models.TextField(unique=False, blank=True, max_length=120)
    quantity = models.Integ`erField(unique=False, validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ] )