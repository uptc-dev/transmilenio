from django.db import models

# CREATE TABLE `sector` (
#   `nombre` varchar(100) NOT NULL

class Sector(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
