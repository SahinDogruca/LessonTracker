from django.contrib import admin
from .models import *


class TodoAdmin(admin.ModelAdmin):
    list_display = ["title", "text", "status", "date"]
    list_display_links = ["title", "text", "status", "date"]
    search_fields = ["title", "text"]
    list_filter = ["status"]


admin.site.register(Todo, TodoAdmin)
