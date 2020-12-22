from django.shortcuts import render
from django.http import HttpResponse
from playlist.models import Song
from emotions.forms import PredictionForm


def startpage(request):
    if request.method == "POST":
        form = PredictionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PredictionForm()
    return render(request, 'start.html', {'form': form})

