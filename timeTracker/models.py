from django.db import models
from datetime import datetime


class Time(models.Model):
    title = models.CharField(max_length=255, verbose_name="Başlık")
    date = models.DateTimeField(
        verbose_name="Tarih", blank=True, null=True, auto_now=True
    )
    hour = models.IntegerField(verbose_name="Saat")
    minute = models.IntegerField(verbose_name="Dakika")

    def __str__(self):
        return (
            self.title if self.title != None or self.title != "" else f"time {self.id}"
        )

    def get_title(self):
        return (
            self.title if self.title != None or self.title != "" else f"time {self.id}"
        )

    def get_time(self):
        return self.date.strftime("%Y:%m:%d:%H:%M:%S")

    def get_weekday(self):
        date = datetime.date(self.date)
        return date.weekday()
    
    def get_formatted_date(self):
        return self.date.strftime("%a, %d %B")
