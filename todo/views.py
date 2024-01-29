from django.shortcuts import render, redirect
from .models import *


def index(request):
    context = {"todos": Todo.objects.all()}
    return render(request, "todo/index.html", context)


def change_status(request, id):
    todo = Todo.objects.get(pk=id)
    print(todo.status)
    if todo.status == "False":
        todo.status = "True"
    else:
        todo.status = "False"
    todo.save()

    return redirect("todoIndex")


def add_todo(request):
    if request.method == "POST":
        todo = Todo()
        todo.title = request.POST["title"]
        todo.text = request.POST["text"]
        todo.status = "False"
        todo.save()
        return redirect("todoIndex")
    return render(request, "todo/add_todo.html")


def delete_todo(request, id):
    Todo.objects.get(pk=id).delete()
    return redirect("todoIndex")


def edit_todo(request, id):
    todo = Todo.objects.get(pk=id)
    if request.method == "POST":
        todo.title = request.POST["title"]
        todo.text = request.POST["text"]
        todo.save()

        return redirect("todoIndex")

    context = {
        "todo": todo,
    }

    return render(request, "todo/edit_todo.html", context)


def back_to_todo(request):
    return redirect("todoIndex")
