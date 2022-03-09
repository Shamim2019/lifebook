from django. shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django. contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView
from.models import Image,editprofile
from .forms import ImageForm, EditForm



def indexView(request):
    return render(request,"index.html")


def registerView(request):
    if request.method == "POST":
       password1=request.POST('password1')
       username=request.POST('username')

       user=User.objects.create_user(username=username,password=password1)
       user.save()
    else:
        return render(request,'registration/register.html')

def dashboardView(request):
    if request.method == "POST":
       form = ImageForm(request.POST,request.FILES)
    if form.is_valid():
           form.save()
    form = ImageForm()
    img = Image.objects.all()
    return render(request,'dashboard.html',{'img':img,'form':form})

def like_api(request):
    print(request.POST["image_id"])
    image=Image.objects.get(id=request.POST["image_id"])
    image.likes.add(request.user)
    return redirect('dashboard')

def unlike_api(request):
    print(request.POST["image_id"])
    image=Image.objects.get(id=request.POST["image_id"])
    user=request.user
    image.unlikes.add(user)
    return redirect('dashboard')

def homeView(request):
    img= img.objects.all()  
    obj = editprofile.objects.all()
    return render(request,'profile.html',{'img':img,'obj':obj}) 

def editView(request):
    if request.method =="POST":
        form=EditForm(request.POST,request.FILES)
        
    if form.is_valid():
        form = EditForm()
    return render (request,'editprofile.html',{'form':form})        