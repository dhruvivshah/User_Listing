#to build a model of the data fetched from randomuser
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
