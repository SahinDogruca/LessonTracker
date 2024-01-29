from django.db import models
from questionTracker.models import Area, Lesson
from datetime import time

# Create your models here.



class Chronometer(models.Model):
    area = models.ForeignKey(
        Area, on_delete=models.CASCADE, verbose_name="Alan", blank=True, null=True
    )
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Ders")
    name = models.CharField(max_length=255, verbose_name="İsim", blank=True, null=True)
    question = models.PositiveIntegerField(verbose_name="Soru Sayısı")
    true = models.IntegerField(verbose_name="Doğru Soru",default=0)
    false = models.IntegerField(verbose_name="Yanlış Soru",default=0)
    minute = models.IntegerField(verbose_name="Dakika")
    second = models.IntegerField(verbose_name="Saniye")
    date = models.DateTimeField(
        verbose_name="Tarih", blank=True, null=True, auto_now=True
    )
    
    def __str__(self):
        return (
            self.name if self.name != None or self.name != "" else f"chronometer {self.id}"
        )

    def get_title(self):
        return (
            self.name if self.name != None or self.name != "" else f"chronometer {self.id}"
        )
    
    def get_formatted_date(self):
        return self.date.strftime("%a, %d %B")
    
    def get_blank_question(self):
        return self.question - (self.true + self.false)

    def get_clear_question(self):
        penalty_question = round(self.false / 4, 2)
        return self.true - (penalty_question)

    def get_time(self):
        return time(0, self.minute, self.second).strftime("%M:%S")
        