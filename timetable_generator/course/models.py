from django.db import models
from teacher.models import Instructor

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=40)
    max_numb_students = models.CharField(max_length=65)
    instructors = models.ManyToManyField(Instructor)

    def __str__(self):
        return f'{self.course_name}'