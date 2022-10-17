from django.shortcuts import render
from .models import employees
# Create your views here.

def people(request):
    if request.method=='GET':
        emp=employees.objects.all()
        return render(request,"display.html",{'emp':emp})
