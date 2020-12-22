from django.db import models


# Create your models here.
class Prediction(models.Model):
    emotion = models.CharField(max_length=30)
    image = models.ImageField(upload_to='PredictionImages')

    def __str__(self):
        return self.emotion
