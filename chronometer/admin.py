from django.contrib import admin
from .models import *


class ChronometerAdmin(admin.ModelAdmin):
    list_display = ["name", "minute", "second", "question", "date"]
    list_display_links = ["name", "minute", "second", "question", "date"]
    search_fields = ["name"]
    list_filter = ["date"]





admin.site.register(Chronometer, ChronometerAdmin)