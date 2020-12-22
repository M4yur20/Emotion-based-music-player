from django.shortcuts import render
from django.http import HttpResponse
from playlist.models import Song
from emotions.forms import PredictionForm


def startpage(request):
    form = PredictionForm()
    return render(request, 'start.html', {'form': form})

