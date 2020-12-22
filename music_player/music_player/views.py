from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'start.html')



def home(request):
    return render(request,'base_layout.html')
