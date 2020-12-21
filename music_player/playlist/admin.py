from django.contrib import admin
from .models import Happy,Angry,Sad,Neutral,Song
# Register your models here.
admin.site.register(Happy)
admin.site.register(Sad)
admin.site.register(Angry)
admin.site.register(Neutral)
admin.site.register(Song)