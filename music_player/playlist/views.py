from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def general(request):
    return HttpResponse("Hello,there !")

def emotion(request,emotion):
    print(type(emotion))
    return HttpResponse(f'{emotion}')
