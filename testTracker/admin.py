from django.contrib import admin
from .models import *
from django.forms.models import BaseInlineFormSet
from django.conf import settings 

tyt = [[5,40], [1,40], [2,7], [3,6], [4,6], [7,5], [6,5], [8,5], [9,5]]
ayt = [[1,40], [2,14], [3,13], [4,13]]

"""
class BranchTestInlineFormset(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        kwargs['initial'] = [{"total_question": tyt[i][1], "lesson": tyt[i][0]} for i in range(0, len(tyt))]
        
        
        
        super(BranchTestInlineFormset, self).__init__(*args, **kwargs)
"""

class BranchTestAdmin(admin.ModelAdmin):
    list_display = [
        "lesson",
        "name",
        "total_question",
        "true_question",
        "false_question",
        "get_blank_question",
        "date",
    ]
    list_display_links = [
        "lesson",
        "name",
        "total_question",
        "true_question",
        "false_question",
        "get_blank_question",
        "date",
    ]


class AreaTestTabularBranch(admin.TabularInline):
    model = BranchTest
    extra = 9
    #formset = BranchTestInlineFormset


class AreaTestAdmin(admin.ModelAdmin):
    list_display = ["area", "name", "visible","date"]
    list_display_links = ["area", "name", "visible","date"]
    inlines = [AreaTestTabularBranch]
    
    
    class Media:
        js = ("js/extra.js",)


admin.site.register(BranchTest, BranchTestAdmin)
admin.site.register(AreaTest, AreaTestAdmin)
