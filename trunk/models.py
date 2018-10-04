from django.db import models

# CREATE TABLE `troncal` (
#   `inicial` varchar(1) NOT NULL,
#   `nombre` varchar(100) NOT NULL,
#   `color_hex` varchar(6) NOT NULL,
#   `longitud_troncal` decimal(10,3) NOT NULL,
#   `longitud_pretroncal` decimal(10,3) NOT NULL,

class Trunk(models.Model):
    first_letter = models.CharField(max_length=1)
    name = models.CharField(max_length=200)
    hex_color = models.CharField(max_length=6)
    trunk_lenght = models.DecimalField(max_digits=10, decimal_places=3)
    pre_trunk_lenght = models.DecimalField(max_digits=10, decimal_places=3)
    def __str__(self):
        return "({}) {}".format(self.first_letter, self.name)
