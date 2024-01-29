from django.contrib import admin
from .models import *


class AreaAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    search_fields = ["name"]


class ClassAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    search_fields = ["name"]


class LessonAdmin(admin.ModelAdmin):
    list_display = ["id","name"]
    list_display_links = ["name"]
    search_fields = ["name"]



class QuestionAdmin(admin.ModelAdmin):
    list_display = ["area", "clas", "lesson", "count", "__str__", "date"]
    list_display_links = ["area", "clas","lesson", "count", "__str__", "date"]
    search_fields = ["__str__"]
    list_filter = ["area", "clas", "lesson", "date"]


admin.site.register(Area, AreaAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
