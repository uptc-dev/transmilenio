from django.db import models

from stations.models import Station

# CREATE TABLE `troncal` (
#   `inicial` varchar(1) NOT NULL,
#   `nombre` varchar(100) NOT NULL,
#   `color_hex` varchar(6) NOT NULL,
#   `longitud_troncal` decimal(10,3) NOT NULL,
#   `longitud_pretroncal` decimal(10,3) NOT NULL,
#   `inicio` bigint(20) NOT NULL,
#   `fin` bigint(20) NOT NULL

class Trunk(models.Model):

    start = models.CharField(max_length=1)
    name = models.CharField(max_length=200)
    hex_color = models.CharField(max_length=6)
    trunk_lenght = models.DecimalField(max_digits=10, decimal_places=3)
    pre_trunk_lenght = models.DecimalField(max_digits=10, decimal_places=3)

    begin = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='begin')
    end =  models.ForeignKey(Station, on_delete=models.CASCADE, related_name='end')

    

