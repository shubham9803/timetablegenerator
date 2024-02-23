from django.shortcuts import render
from .models import Instructor

# Create your views here.

def teacher(request):
    if request.method == 'POST':
        request_from_delete = request.POST.get('request_from_delete')
        if request_from_delete is None:
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            new_teacher = Instructor.objects.create(first_name = fname, last_name = lname)
            new_teacher.save()
        else:
            teacher =Instructor.objects.get(id =request_from_delete)
            teacher.delete()    
    all_teacher_data = Instructor.objects.all()
    context = {
        'all_teacher' : all_teacher_data,
        'page_title':'Teacher'
    }
    return render(request,'teacher.html',context)