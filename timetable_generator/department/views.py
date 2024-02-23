from django.shortcuts import render
from course.models import Course
from .models import Department

# Create your views here.
def department(request):
      if request.method == 'POST':
            request_from_delete = request.POST.get('request_from_delete')
            if request_from_delete is None:
                  d_name = request.POST.get('dname')
                  d_courses = request.POST.getlist('dcourses')
                  new_dept = Department.objects.create(dept_name = d_name)
                  for course in d_courses:
                        new_dept.courses.add(course)
                  new_dept.save()      
            else:
                  dept = Department.objects.get(id=request_from_delete)
                  dept.delete()
      all_depts = Department.objects.all()            
      all_courses = Course.objects.all()  
      context = {
              'all_depts':all_depts,
              'all_courses':all_courses,
              'page_title':'Department'
      }
      return render(request,'department.html',context)