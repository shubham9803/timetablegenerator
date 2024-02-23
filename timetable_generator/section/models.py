from django.db import models
from department.models import Department
from course.models import Course
from meeting.models import MeetingTime
from room.models import Room
from teacher.models import Instructor

# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length=30,default="Section 1")
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    num_class_in_week = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    meeting_time = models.ForeignKey(MeetingTime, on_delete=models.CASCADE, blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, blank=True, null=True)

    def set_room(self, room):
        section = Section.objects.get(id = self.id)
        section.room = room
        section.save()

    def set_meetingTime(self, meetingTime):
        section = Section.objects.get(id = self.id)
        section.meeting_time = meetingTime
        section.save()

    def set_instructor(self, instructor):
        section = Section.objects.get(id=self.id)
        section.instructor = instructor
        section.save()