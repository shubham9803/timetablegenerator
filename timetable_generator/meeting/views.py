from django.shortcuts import render
from .models import MeetingTime

# Create your views here.
def meeting(request):
    if request.method =="POST":
        request_from_delete = request.POST.get("request_from_delete")
        if request_from_delete is None:
            m_name = request.POST.get('mname')
            m_time = request.POST.get('mtime')
            m_day = request.POST.get('mday')
            new_meeting = MeetingTime.objects.create(meeting_name = m_name, meeting_time = m_time, meeting_day = m_day)
            new_meeting.save()
        else:
            meeting1 = MeetingTime.objects.get(id = request_from_delete)    
            meeting1.delete()
    all_meeting_data = MeetingTime.objects.all()        
    context = {
        'all_meetings':all_meeting_data,
        'page_title':"Meeting"
    }
    return render(request,'timing.html',context)