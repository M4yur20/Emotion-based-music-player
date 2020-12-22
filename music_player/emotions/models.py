from django.db import models

# Create your models here.
class Prediction(models.Model):
    image=models.ImageField()
    emotion=models.CHarField(max_length=30)