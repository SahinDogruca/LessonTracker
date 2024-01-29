from django.contrib import admin
from .models import *


class TimeAdmin(admin.ModelAdmin):
    list_display = ["title", "date", "hour", "minute"]
    list_display_links = ["title", "date", "hour", "minute"]
    search_fields = ["title"]
    list_filter = ["date"]





admin.site.register(Time, TimeAdmin)
