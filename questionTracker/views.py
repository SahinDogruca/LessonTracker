from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

# TODO filter yaptıktan sonra seçimleri seçili kalmasını sağla


def index(request):
    questions = get_questions("week")

    areasList = []
    classesList = []
    lessonsList = []
    for question in questions:
        lessonsList.append(question.lesson_id)
        classesList.append(question.clas_id)
        areasList.append(question.area_id)

    areas = Area.objects.filter(pk__in=areasList)
    classes = Class.objects.filter(pk__in=classesList)
    lessons = Lesson.objects.filter(pk__in=lessonsList)

    context = {
        "areas": areas,
        "classes": classes,
        "lessons": lessons,
        "questions": questions,
    }
    return render(request, "questionTracker/index.html", context)


def add_question(request):
    questions = Question.objects.all()
    if request.method == "POST":
        area = request.POST["area"]
        clas = request.POST["class"]
        lesson = request.POST["lesson"]
        count = request.POST["count"]

        question = Question()
        question.area_id = area
        question.clas_id = clas
        question.lesson_id = lesson
        question.count = count
        question.name = request.POST["name"]
        question.date = datetime.now()
        question.save()

        return redirect("questionTrackerIndex")

    context = {
        "areas": Area.objects.all(),
        "classes": Class.objects.all(),
        "lessons": Lesson.objects.all(),
    }

    return render(request, "questionTracker/add_question.html", context)


def edit_question(request, id):
    question = Question.objects.get(pk=id)
    if request.method == "POST":
        question.area_id = request.POST["area"]
        question.clas_id = request.POST["class"]
        question.lesson_id = request.POST["lesson"]
        question.count = int(request.POST["count"])
        question.name = request.POST["name"]
        question.save()

        return redirect("questionTrackerIndex")

    context = {
        "areas": Area.objects.all(),
        "classes": Class.objects.all(),
        "lessons": Lesson.objects.all(),
        "question": question,
    }

    return render(request, "questionTracker/edit_question.html", context)


def delete_question(request, id):
    Question.objects.get(pk=id).delete()
    return redirect("questionTrackerIndex")


def filter_question(request):
    if request.method == "POST":
        questions = None
        date = request.POST["date"]

        if date != "":
            questions = get_questions(date)
        area = request.POST["area"]
        if area != "":
            questions = Question.objects.filter(area_id=area)
        clas = request.POST["class"]
        if clas != "":
            questions = Question.objects.filter(clas_id=clas)
        lesson = request.POST["lesson"]
        if lesson != "":
            questions = Question.objects.filter(lesson_id=lesson)

        if questions == None:
            return redirect("questionTrackerIndex")

        questionsList = get_questions("week")

        areasList = []
        classesList = []
        lessonsList = []
        for question in questionsList:
            lessonsList.append(question.lesson_id)
            classesList.append(question.clas_id)
            areasList.append(question.area_id)

        areas = Area.objects.filter(pk__in=areasList)
        classes = Class.objects.filter(pk__in=classesList)
        lessons = Lesson.objects.filter(pk__in=lessonsList)

        context = {
            "areas": areas,
            "classes": classes,
            "lessons": lessons,
            "questions": questions,
        }

        return render(request, "questionTracker/index.html", context)


def get_date_infos():
    today = datetime.now()

    year = today.year
    month = today.month
    week = today.isocalendar()[1]
    day = today.day

    info = {"year": year, "month": month, "week": week, "day": day}

    return info


def get_questions(date_info):
    info = get_date_infos()

    result_info = info.get(date_info)
    month = info.get("month")

    if date_info == "year":
        questions = Question.objects.filter(date__year=result_info)
    elif date_info == "month":
        questions = Question.objects.filter(date__month=result_info)
    elif date_info == "week":
        questions = Question.objects.filter(date__week=result_info)
    elif date_info == "day":
        questions = Question.objects.filter(date__day=result_info, date__month= month)

    return questions
