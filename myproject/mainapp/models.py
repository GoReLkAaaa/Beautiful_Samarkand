""" Import your model here"""

from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True, null=True)



    def __str__(self):
        return self.name


