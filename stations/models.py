from django.db import models

# from trunk.models import Trunk

#     CREATE TABLE `estacion` (
#   `nombre` varchar(100) NOT NULL,
#   `ubication` point NOT NULL,
#   `troncal` bigint(20) NOT NULL

class Station(models.Model):

    name = models.CharField(max_length=200)

    latitude = models.DecimalField(max_digits=25, decimal_places=20)
    longitude = models.DecimalField(max_digits=25, decimal_places=20)

    # trunk = models.ForeignKey(Trunk, on_delete=models.CASCADE)


