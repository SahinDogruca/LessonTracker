from django.db import models
from questionTracker.models import Area, Class, Lesson


class Subject(models.Model):
    STATUS = (("True", "True"), ("False", "False"))
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="Alan")
    clas = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name="Sınıf")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Ders")
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        verbose_name="Parent",
        blank=True,
        null=True,
        related_name="children",
    )
    name = models.CharField(max_length=255, verbose_name="Isim")
    status = models.CharField(choices=STATUS, verbose_name="Durum", max_length=10)

    def __str__(self):
        return self.name

    def get_title(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return " -> ".join(full_path[::-1])

    def get_name(self):
        return self.name
