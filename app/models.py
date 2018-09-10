"""
Definition of models.
"""

from django.db import models
# Create your models here.

class Album(models.Model):
    name=models.CharField('Artist',max_length=40)
    year_formed=models.CharField(max_length=40)
    description=models.CharField(max_length=50)

class Artist(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    name=models.CharField('Album',max_length=40)
    description=models.CharField(max_length=50)


