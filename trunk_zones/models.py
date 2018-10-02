from django.db import models

from trunk.models import Trunk

from zones.models import Zone

# CREATE TABLE `zona_troncal` (
#   `troncal` bigint(20) NOT NULL,
#   `zona` bigint(20) NOT NULL
# );

class Trunk_zone(models.Model):

    trunk = models.ForeignKey(Trunk, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)


