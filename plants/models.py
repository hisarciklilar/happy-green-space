from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Plant(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plants')
    plant_name = models.CharField(max_length=100)
    date_planted = models.DateField(null=True, blank=True)
    grew_well = models.BooleanField("Did the plant grow well?", default=False)
    notes = models.TextField(blank=True)
