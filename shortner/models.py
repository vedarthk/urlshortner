from django.db import models

# Create your models here.

class Shortener(models.Model):

    url = models.URLField(max_length = 2047)
    key = models.CharField(max_length = 4)
    shortcode = models.CharField(max_length = 10, unique = True)
