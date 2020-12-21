from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Happy(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)


class Angry(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class Sad(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class Neutral(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class Song(models.Model):
    name=models.CharField(max_length=30,default="Unknown",blank=True)
    track=models.FileField()
    happy=models.OneToOneField(Happy,on_delete=models.CASCADE)
    angry=models.OneToOneField(Angry,on_delete=models.CASCADE)
    sad=models.OneToOneField(Sad,on_delete=models.CASCADE)
    neutral=models.OneToOneField(Neutral,on_delete=models.CASCADE)
