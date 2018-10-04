from django.db import models

from trunk.models import Trunk
from stations.models import Station

# CREATE TABLE `transferencia` (
#   `troncal` bigint(20) NOT NULL,
#   `transferencia` bigint(20) NOT NULL,
#   `estacion` bigint(20) NOT NULL


class Transfer(models.Model):

    trunk = models.ForeignKey(Trunk, on_delete=models.CASCADE, related_name='trunk')
    transfer = models.ForeignKey('self', on_delete=models.CASCADE, related_name='transfer_accessor')
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='station')
