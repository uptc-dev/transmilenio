from django.db import models

from zones.models import Zone
from tracks.models import Track

# CREATE TABLE `limites` (
#   `zona` bigint(20) NOT NULL,
#   `via` bigint(20) NOT NULL

class Limit(models.Model):

    zone = models.ForeignKey(Zone, on_delete=models.CASCADE) # Evaluar si es mejor one to one Field primary_key=True
    track = models.ForeignKey(Track, on_delete=models.CASCADE) # Evaluar si es mejor one to one Field primary_key=True

    
