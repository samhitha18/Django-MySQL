from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class employees(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    department = models.CharField(max_length=15)