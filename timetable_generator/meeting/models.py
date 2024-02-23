from django.db import models

# Create your models here.

class MeetingTime(models.Model):
    meeting_name = models.CharField(max_length=30)
    meeting_time = models.CharField(max_length=50, default='11:30 - 12:30')
    meeting_day = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.meeting_name} {self.meeting_time} {self.meeting_day}' 