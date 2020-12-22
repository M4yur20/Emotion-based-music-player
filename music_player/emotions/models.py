from django.db import models


# Create your models here.
class Prediction(models.Model):
<<<<<<< Updated upstream
    image = models.ImageField()
    emotion = models.CHarField(max_length=30)
=======
    image = models.ImageField(upload_to='Prediction_Images')
>>>>>>> Stashed changes
