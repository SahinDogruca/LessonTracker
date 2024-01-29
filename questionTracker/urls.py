from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="questionTrackerIndex"),
    path("add-question", views.add_question, name="addQuestion"),
    path("delete-question/<int:id>", views.delete_question, name="deleteQuestion"),
    path("edit-question/<int:id>", views.edit_question, name="editQuestion"),
    path("filter-question", views.filter_question, name="filterQuestion"),
]
