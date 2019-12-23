from django.db import models

# Create your models here.
from django.db import models
from decimal import Decimal

class Category(models.Model) :
    name = models.CharField(max_length=128)
    def __str__(self) :
        return self.name
class States(models.Model):
    name=models.CharField(max_length=128)
    def __str__(self) :
        return self.name
class Region(models.Model):
    name=models.CharField(max_length=128)
    def __str__(self) :
        return self.name
class ISO(models.Model):
    name=models.CharField(max_length=128)
    def __str__(self) :
        return self.name
class Site(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    description=models.CharField(max_length=1024)
    justification=models.CharField(max_length=1024)
    #longtitude=models.DecimalField(null=True)
    #latitude=models.DecimalField(null=True)
    #area_hectares=models.DecimalField(null=True)
    longitude=models.DecimalField(max_digits=19, decimal_places=10, blank=True, null=True)
    latitude=models.DecimalField(max_digits=19, decimal_places=10, blank=True, null=True)
    area_hectares=models.DecimalField(max_digits=19, decimal_places=10, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    states=models.ForeignKey(States, on_delete=models.CASCADE)
    region=models.ForeignKey(Region, on_delete=models.CASCADE)
    iso=models.ForeignKey(ISO, on_delete=models.CASCADE)
    def __str__(self) :
        return self.name
