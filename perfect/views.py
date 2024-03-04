from django.shortcuts import render, redirect
from .models import Employees
# Create your views here.
def index(request):
    data = Employees.objects.all()
    context = {"data":data}
    return render(request,"index.html", context)
def insertdata(request):
    if request.method == "POST":


        if len(request.FILES) != 0:
            image = request.FILES['image']

            query = Employees(name=name, email=email, gender=gender, image=image)
            query.save()
            return redirect("/")


        return  render(request,'index.html')

def updatedata(request,id):
    if request.method == "POST":
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        email = request.POST.get('email')

        edit = Employees.objects.get(id=id)
        edit.name = name
        edit.age = age
        edit.gender = gender
        edit.email = email
        if len(request.FILES != 0:
            if len(edit.image) > 0:\
                edit.image = request.FILES['image']
        edit.save()
        return redirect("/")
    d=Employees.objects.get(id=id)
    context ={"d":d}
    return  render(request, 'edit.html',context)
def deletedata(request, id):
    d = Employees.objects.get(id=id)
    d.delete()
    return  redirect("/")
    return  render(request,"index.html")



