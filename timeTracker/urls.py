from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="timeTrackerIndex"),
    path("filter-time", views.filter_time, name="filterTime"),
    path("delete-time/<int:id>", views.delete_time, name="deleteTime"),
    path("edit-time/<int:id>", views.edit_time, name="editTime"),
    path("add-time", views.add_time, name="addTime"),
    path("back-to-time", views.back_to_time, name="backToTime"),
]
