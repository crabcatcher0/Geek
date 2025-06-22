from django.db import models
from django.core.validators import MaxValueValidator

class SquadPowerEntry(models.Model):
    in_game_name = models.CharField(max_length=100)
    hq_level = models.PositiveIntegerField(
    validators=[MaxValueValidator(30)])
    squad_power = models.DecimalField(max_digits=5, decimal_places=3)
    image = models.ImageField(upload_to='squad_images/') 
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.in_game_name} (HQ {self.hq_level}) - Squad Power: {self.squad_power}"

