from django.shortcuts import render
from .models import Plant_Details
from .forms import PlantDetailsForm
from django.http import HttpResponseRedirect

# Create your views here.
def insert(request):
    f=PlantDetailsForm()
    if(request.method=="POST"):
        f=PlantDetailsForm(request.POST)
        f.save()
        return HttpResponseRedirect('/show')
    return render(request,"insert.html",{'form':f})
def show(request):
    f=Plant_Details.objects.all()
    return render(request,"show.html",{'plantf':f})
def update2(request):
    
    return render(request,"update2.html")
def update(request):
    t=str(request.GET["name1"])
    plantobj=Plant_Details.objects.filter(plant_name=t).first()
    f=PlantDetailsForm(instance=plantobj)
    if(request.method=="POST"):
        f=PlantDetailsForm(request.POST,instance=plantobj)
        f.save()
        return HttpResponseRedirect('/show')
    return render(request,"update.html",{'form':f})
def home(request):
    return render(request,"home.html")
    
                                    
