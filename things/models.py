from django.db import models
from django.db.models import Model
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Thing(AbstractUser):
    bio = models.TextField()
    quantity = models.PositiveIntegerField()
    description = models.TextField()
