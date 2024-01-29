from django.db import models


class Todo(models.Model):
    STATUS = (("True", "True"), ("False", "False"))
    title = models.CharField(
        max_length=255, verbose_name="Başlık", null=True, blank=True
    )
    text = models.CharField(max_length=255, verbose_name="Yapılacak Is")
    status = models.CharField(choices=STATUS, max_length=10, verbose_name="Durum")
    date = models.DateTimeField(verbose_name="Tarih", blank=True, null=True, auto_now=True)

    def __str__(self):
        return self.title

    def get_time(self):
        return self.date.strftime("%Y:%m:%d:%H:%M:%S")
