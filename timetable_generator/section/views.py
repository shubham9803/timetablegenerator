from django.shortcuts import render
from department.models import Department
from .models import Section
# Create your views here.
def section(request):
      if request.method == 'POST':
            request_from_delete = request.POST.get('request_from_delete')
            if request_from_delete is None:
                  s_name =request.POST.get('sname')
                  s_dept = Department.objects.get(id = request.POST.get('sdept'))
                  s_lec = request.POST.get('slec')
                  print(s_name,s_dept,s_lec)
                  new_section = Section.objects.create(name = s_name,department = s_dept,num_class_in_week =s_lec )
                  new_section.save()
            else:
                  section = Section.objects.get(id = request_from_delete)    
                  section.delete()  
      all_sections = Section.objects.all()
      all_depts = Department.objects.all()
      context = {
            'all_sections':all_sections,
            'all_depts':all_depts,
            'page_title':'Section'
      }
      return render(request,'section.html',context)