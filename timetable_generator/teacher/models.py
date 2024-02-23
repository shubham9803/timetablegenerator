from django.db import models

# Create your models here.
class Instructor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}' # here i have to return fname and lname 