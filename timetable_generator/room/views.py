from django.shortcuts import render
from .models import Room

# Create your views here.
def room(request):
   if request.method == 'POST':
      request_from_delete = request.POST.get('request_from_delete')
      if request_from_delete is None:
         r_name = request.POST.get('rname')
         r_num = request.POST.get('rnum')
         r_cap = request.POST.get('rcap')
         new_room = Room.objects.create(room_name = r_name, room_number = r_num, room_capacity = r_cap)
         new_room.save()
      else:
         room = Room.objects.get(id=request_from_delete)
         room.delete()
   all_room_data = Room.objects.all()
   context = {
      'all_rooms':all_room_data,
       'page_title':"Room" 
    }
   return render(request,'room.html',context)