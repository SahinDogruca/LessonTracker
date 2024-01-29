from django.shortcuts import render, redirect
from questionTracker.models import Area, Class, Lesson
from .models import Subject


def index(request):
    context = {
        "areas": Area.objects.all(),
        "classes": Class.objects.all(),
        "lessons": Lesson.objects.all(),
        "subjects": Subject.objects.all(),
    }
    return render(request, "subjectTracker/index.html", context)


def delete_subject(request, id):
    Subject.objects.get(pk=id).delete()
    return redirect("subjectTrackerIndex")


def change_status_subject(request, id):
    subject = Subject.objects.get(pk=id)

    for subsubject in subject.children.all():
        if subsubject.parent.status != subsubject.status:
            continue
        if subsubject.status == "False":
            subsubject.status = "True"
        else:
            subsubject.status = "False"
        subsubject.save()

    if subject.status == "False":
        subject.status = "True"
    else:
        subject.status = "False"
    subject.save()

    return redirect("subjectTrackerIndex")


def back_to_subject(request):
    return redirect("subjectTrackerIndex")


def filter_subject(request):
    if request.method == "POST":
        subjects = None
        area = request.POST["area"]
        if area != "":
            subjects = Subject.objects.filter(area_id=area)
        clas = request.POST["class"]
        if clas != "":
            subjects = Subject.objects.filter(clas_id=clas)
        lesson = request.POST["lesson"]
        if lesson != "":
            subjects = Subject.objects.filter(lesson_id=lesson)

        if subjects == None:
            return redirect("subjectTrackerIndex")

        subjectsList = Subject.objects.all()

        areasList = []
        classesList = []
        lessonsList = []
        for subject in subjectsList:
            lessonsList.append(subject.lesson_id)
            classesList.append(subject.clas_id)
            areasList.append(subject.area_id)

        areas = Area.objects.filter(pk__in=areasList)
        classes = Class.objects.filter(pk__in=classesList)
        lessons = Lesson.objects.filter(pk__in=lessonsList)

        context = {
            "areas": areas,
            "classes": classes,
            "lessons": lessons,
            "subjects": subjects,
        }

        return render(request, "subjectTracker/index.html", context)
