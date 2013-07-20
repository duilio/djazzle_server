from django.db import models


class Track(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    data = models.FileField(upload_to='tracks/')
    reversed_data = models.FileField(upload_to='reverse_tracks/', null=True, blank=True)
