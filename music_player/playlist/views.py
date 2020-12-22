from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Song
from .forms import *


# Create your views here.
def general(request):
    user = request.user
    songs = Song.objects.all().filter(user=user)
    return render(request, 'playlist/general.html', {'songs': songs})


def emotion(request, type):
    user = request.user
    songs = Song.objects.all().filter(user=user, type=type)
    dic = {0: 'Happy',
           1: 'Angry',
           2: 'Sad',
           3: 'Neutral'}
    return render(request, 'playlist/type.html', {'songs': songs, 'type': dic[type]})


@login_required(login_url='accounts:login')
def song_upload(request):
    if request.method == "POST":
        form = SongUploadForm(request.POST, request.FILES)
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('home')
    else:
        form = SongUploadForm()
    return render(request, 'playlist/song_upload.html', {'form': form})
