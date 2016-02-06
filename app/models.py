from django.db import models

class ShortenedURL(models.Model):
    url = models.CharField(max_length=1000)
    shortened = models.CharField(max_length=200)
