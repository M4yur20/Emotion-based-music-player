from django.contrib.auth.models import User
from django.db import models


class Song(models.Model):
    choices = ((0, 'happy'),
               (1, 'angry'),
               (2, 'sad'),
               (3, 'neutral'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.FileField()
    type = models.IntegerField(choices)
    name = models.CharField(max_length=30, default="Unknown", blank=True)
