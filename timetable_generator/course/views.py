from django.shortcuts import render
from teacher.models import Instructor
from .models import Course
# Create your views here.
def course(request):
    if request.method == "POST":
      request_from_delete =request.POST.get('request_from_delete')
      print(request_from_delete)
      if request_from_delete is None: 
        c_name = request.POST.get('cname')
        c_max_stud = request.POST.get('ccap')
        c_teachers = request.POST.getlist('cteachers')
        new_course = Course.objects.create(course_name =c_name,max_numb_students =c_max_stud)
        for teacher in c_teachers:
              new_course.instructors.add(teacher)
        new_course.save()
      else:
        course = Course.objects.get(id=request_from_delete) 
        print(course) 
        course.delete()
    all_teachers = Instructor.objects.all()
    all_courses = Course.objects.all()
    context = {
      'all_courses':all_courses,
      'all_teachers':all_teachers,
          'page_title':'Course'
    }
    return render(request,'course.html',context)