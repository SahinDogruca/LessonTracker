from datetime import date
from django.db import models
from questionTracker.models import *

# Create your models here.



class Status(models.Model):
    name = models.CharField(verbose_name="Adı", null=False, blank=False, max_length=255)

    def __str__(self):
        return self.name


class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
    
    title = models.CharField(verbose_name="Başlık", null=True, blank=True, max_length=255)
    
    area = models.ForeignKey(
        Area, on_delete=models.SET_NULL, null=True, blank=True)
    
    lesson = models.ForeignKey(
        Lesson, on_delete=models.SET_NULL, null=True, blank=True)
    
    status = models.ForeignKey(
        Status, on_delete=models.SET_NULL, null=True, blank=True)


    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    date = models.DateTimeField(verbose_name="Tarih", auto_now_add=True)

    def __str__(self):
        return self.title
