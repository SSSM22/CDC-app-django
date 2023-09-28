from django.shortcuts import render,HttpResponse
from django.db import connection
from .models import R21
import requests
from bs4 import BeautifulSoup
# Create your views here.
def index(request):
    return render(request,'index.html')
   
def display_students(request,year,br):
    
    if(year=='3rd'):
        if(br!='all'):
            students=R21.objects.all().order_by('-overall_score').filter(branch=br)
            return students

        students = R21.objects.all().order_by('-overall_score')    
    if(year=='2nd'):    
        if(br!='all'):
            students=R22.objects.all().order_by('-overall_score').filter(branch=br)
            return students

        students = R22.objects.all().order_by('-overall_score') 
    if(year=='1st'):    
        if(br!='all'):
            students=R23.objects.all().order_by('-overall_score').filter(branch=br)
            return students

        students = R23.objects.all().order_by('-overall_score') 

    if(year=='4th'):    
        if(br!='all'):
            students=R20.objects.all().order_by('-overall_score').filter(branch=br)
            return students

        students = R20.objects.all().order_by('-overall_score')     
    
    return students
    #return render(request,'display.html',context)
   
    ''' with connection.cursor() as cursor:
        cursor.callproc('get_det')
        results = cursor.fetchall()
        print(results)
    '''

def validate(request):
    if request.method=='POST':
        details = request.POST.dict()
        year=details['year']
        branch=details['branch']
        print(year,branch)

        students=display_students(request,year,branch)
        context={
        'students':students
        }
        return render(request,'display.html',context)
    




