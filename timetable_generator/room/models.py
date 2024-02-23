from django.db import models

# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=30)
    room_number = models.CharField(max_length=6)
    room_capacity = models.IntegerField(default=30)