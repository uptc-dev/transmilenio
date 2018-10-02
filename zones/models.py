from django.db import models

# CREATE TABLE `zona` (
#   `nombre` varchar(100) NOT NULL,
#   `sector` bigint(20) NOT NULL

class Zone(models.Model):

    name = models.CharField(max_length=200)
    # sector =
   

