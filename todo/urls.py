from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="todoIndex"),
    path("change-status/<int:id>", views.change_status, name="changeStatus"),
    path("add-todo", views.add_todo, name="addTodo"),
    path("delete-todo/<int:id>", views.delete_todo, name="deleteTodo"),
    path("edit-todo/<int:id>", views.edit_todo, name="editTodo"),
    path("back-to-todo", views.back_to_todo, name="backToTodo"),
]
