from django.db import models

# CREATE TABLE `via` (
#   `nombre` varchar(100) NOT NULL

class Track(models.Model):

    name = models.CharField(max_length=200)

