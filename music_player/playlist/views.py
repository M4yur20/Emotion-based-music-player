from django.shortcuts import render
from django.http import HttpResponse
from .models import Song

# Create your views here.
def general(request):
    user=request.user
    songs=Song.objects.all().filter(user=user)
    return render(request,'playlist/general.html',{'songs':songs})
    

def emotion(request,type):
    user=request.user
    songs=Song.objects.all().filter(user=user,type=type)
    dic={0:'Happy',
        1:'Angry',
         2:'Sad',
         3:'Neutral'}
    return render(request,'playlist/type.html',{'songs':songs,'type':dic[type]})
    
