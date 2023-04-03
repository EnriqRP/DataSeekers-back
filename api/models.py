from django.db import models

# Create your models here.

class Users (models.Model):
    name = models.CharField(max_length=60)
    connections = models.CharField(max_length=300)

