from django.forms.widgets import DateTimeInput
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import logout,login,authenticate
from .forms import SignUpForm
from django.contrib import messages
from .models import Contact
# from django.contrib.auth.models import SignUp
# Create your views here.

def home(request):
    if request.method=='POST' and "Submit2" in request.POST:
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,'Account created Successfully !!')
    elif request.method=='POST' and "Submit1" in request.POST:
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('base')
            else:
                return redirect('home')
    else:
        fm=SignUpForm ()
    return render(request,'home.html',{'form':fm})
 

def base(request):
    if request.user.is_authenticated:
        return render(request,'base.html',{'name':request.user})
    else:
        return redirect('home')

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=DateTimeInput.today())
        contact.save() 
        messages.success(request, 'Your message has been sent.')
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def user_logout(request):
    logout(request)
    return redirect('home')