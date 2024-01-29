from django.db import models
from django.utils.text import slugify
from datetime import datetime


class Area(models.Model):
    name = models.CharField(max_length=255, verbose_name="Isim")

    def __str__(self):
        return self.name

    def to_slug_format(self):
        return slugify(self.name)


class Class(models.Model):
    name = models.CharField(max_length=255, verbose_name="Isim")

    def __str__(self):
        return self.name

    def to_slug_format(self):
        return slugify(self.name)


class Lesson(models.Model):
    name = models.CharField(max_length=255, verbose_name="Isim")

    def __str__(self):
        return self.name

    def to_slug_format(self):
        return slugify(self.name)


class Question(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="Alan")
    clas = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name="Sınıf", blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Ders", blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name="Isim", blank=True, null=True)
    count = models.IntegerField(verbose_name="Soru Sayısı")
    date = models.DateTimeField(verbose_name="Tarih", blank=True, null=True, auto_now=True)

    def __str__(self):
        return self.name if self.name != None else f"Soru {self.id}"

    def get_time(self):
        return self.date.strftime("%Y:%m:%d:%H:%M:%S")

    def get_weekday(self):
        date = datetime.date(self.date)
        return date.weekday()
       
    def get_formatted_date(self):
        return self.date.strftime("%a, %d %B")
