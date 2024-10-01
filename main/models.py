from django.db import models
import uuid
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

    
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('out_of_stock', 'Out of Stock'),
        ('discontinued', 'Discontinued'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return self.name
    
class Project(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    name = models.CharField(max_length=255)


class Employee(models.Model):
    department = models.CharField(max_length=100)
    projects = models.ManyToManyField(Project)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

