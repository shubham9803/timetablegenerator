from django.shortcuts import render,HttpResponseRedirect,redirect,reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def signin(request):
    if request.user.is_authenticated:
        user=request.user
        return HttpResponseRedirect(reverse('home'))
     
    if request.method == 'POST':
        
        email = request.POST['email']
        password = request.POST['password']
        print("got the username and password...")
        if "@" not in email:
            messages.error(request,"Invalid email")
            return redirect('signin')
        else:
         username=email[:email.index("@")]    
         user = authenticate(request, username=username, password=password)
         if user is not None:
             print("user is authenticated...")
             login(request, user)
             return HttpResponseRedirect(reverse('home')) 
         else:
          print("user is getting none")  
          messages.error(request,"Invalid email or password")
          return redirect('signin')
  
   
    return render(request,'sign-in.html')

def signup(request):
    if request.user.is_authenticated:
      user=request.user
      return HttpResponseRedirect(reverse('home'))

    if request.method=='POST':
      fname = request.POST['fname'].strip()
      lname = request.POST['lname'].strip()
      email=request.POST['email']
      password=request.POST['password']
      confirm_password=request.POST['confirm-password']
      
      
      if fname !='' and lname != '' and  email != '' and fname is not None and lname is not None and email is not None and password is not None and confirm_password is not None and email.__contains__('@'):
        if password==confirm_password:
          if User.objects.filter(email=email).exists():
           messages.error(request,"email already exists")
           return redirect('signup')
          else:
           username=email[:email.index("@")]
           user=User.objects.create_user(username=username ,email=email,password=password,first_name=fname,last_name = lname)   
           user.save()
           messages.success(request,"signup successfull")
          return redirect('signin')
        else:
           messages.error(request,"Password did not match")  
      else: 
        messages.error(request,"Fill all the fields correctly ")  

    return render(request,'sign-up.html')

@login_required
def signout(request):
    logout(request)
    return redirect('signin')