from django.contrib import admin
from .models import Subject


class SubjectAdmin(admin.ModelAdmin):
    list_display = ["area", "clas", "lesson", "name", "status"]
    list_display_links = ["area", "clas", "lesson", "name", "status"]
    search_fields = ["name"]
    list_filter = ["area","clas","lesson","status"]


admin.site.register(Subject, SubjectAdmin)
