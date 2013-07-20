from django.db import models


class Track(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    data = models.FileField(upload_to='tracks/')
