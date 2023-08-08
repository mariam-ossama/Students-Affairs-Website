from http.client import HTTPResponse
import django
from django.shortcuts import render 
from .models import student

def home (request):
    return render(request,'the first homepage.html')

def index (request):
    return render(request,'homepage.html')

def allstudent (request):
    return render(request,'view all student.html',{'students':student.objects.all()})

def activestudent (request):
    return render(request,'view active student.html',{'students':student.objects.all()})

def inactivestudent (request):
    return render(request,'view inactive student.html',{'students':student.objects.all()})    

def addstudent (request):
    if request.method == 'POST':
        name = request.POST['name']
        id = request.POST['id']
        level= request.POST['level']
        department= request.POST['department']
        GPA= request.POST['gpa']
        status= request.POST['status']
        gender=request.POST['gender']
        Email=request.POST['email']
        Date_of_birth=request.POST['dateOfBirth']
        phoneNumber= request.POST['phoneNumber']

        new_student =student (name=name, id=id, level=level, department=department, GPA=GPA,  status=status, gender=gender, Email=Email,Date_of_birth=Date_of_birth,phoneNumber=phoneNumber )
        new_student.save()
    return render(request,'add_student.html')

def search (request):
     if 'name' in request.GET:
         name =request.GET['name']
         request.session['test']=name 
         students=student.objects.filter(name__icontains=name)
     else:  
       students=student.objects.all()
     return render(request, 'search.html',{'students':students})

def show(request):
    if request.session['test']!=None :
        stu=student.objects.filter(name__icontains= request.session['test'])   
        request.session= None 
        return render (request,'show search results.html',{'searchedstu':stu})  
    else:
       return render (request,'show search result.html')     
        
def update(request):
     return render(request,'update.html')

def assigndepartment(request):
    return render(request,'student department assignment.html')

def createorder(request):
    context={}
    return render(request, 'orderform.html',context)