from django.contrib import admin
from django.urls import path,include
from . import views
app_name='playlist'

urlpatterns = [
        path('',views.general,name='general'),
        path('<int:type>/',views.emotion,name='emotion'),
        path('songupload/<int:type>/',views.song_upload,name='songupload'),
        path('up-song/',views.up_song,name='song'),
]
