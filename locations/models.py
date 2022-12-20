from django.contrib.gis.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    coordinates = models.PointField()