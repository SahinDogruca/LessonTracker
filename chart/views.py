from django.shortcuts import render
from questionTracker.models import Question
from datetime import datetime
from django.http import JsonResponse
from calendar import monthrange
from timeTracker.models import Time


def question_chart_of_week(request):
    context = {
        "date": datetime.now().strftime("%d %B %Y %A")
    }
    return render(request, "chart/question_chart_of_week.html", context)


def question_chart_of_month(request):
    context = {
        "date": datetime.now().strftime("%d %B %Y %A")
    }
    return render(request, "chart/question_chart_of_month.html", context)


def question_count_week(request):
    data = []

    questions = Question.objects.filter(date__week=datetime.now().isocalendar()[1])

    for question in questions:
        value = {
            "day": question.get_weekday(),
            "count": question.count,
        }
        data.append(value)

    days_of_week = data_to_list_week(data)

    return JsonResponse(data={"data": days_of_week})


def question_count_month(request):
    data = []
    labels = []
    today = datetime.now().day

    questions = Question.objects.filter(date__month=datetime.now().month)

    for question in questions:
        day = int(question.date.strftime("%d"))
        count = 0
        if day <= today:
            count = question.count
        value = {
            "day": day,
            "count": count,
        }
        data.append(value)

    days_of_month = data_to_list_month(data)[1]
    labels = data_to_list_month(data)[0]

    return JsonResponse(data={"data": days_of_month, "labels": labels})


def data_to_list_week(data):
    days_of_week = [0] * 7

    for i in range(0, len(data)):
        day = data[i].get("day")
        value = data[i].get("count")
        days_of_week[day] += int(value)

    return days_of_week


def data_to_list_month(data):
    today = datetime.now()
    days_of_month = list(monthrange(today.year, today.month))[1]

    labels = [i for i in range(0, days_of_month + 1)]

    list_of_month = [0] * (days_of_month + 1)

    for i in range(0, len(data)):
        day = data[i].get("day")
        value = data[i].get("count")
        """if i == 0:
            day = 0
            value = 0"""
        

        list_of_month[day] += value

    return [labels, list_of_month]


def time_count_week(request):
    data = []
    times = Time.objects.filter(date__week=datetime.now().isocalendar()[1])

    for time in times:
        value = {
            "day": time.get_weekday(),
            "count": time.minute + (time.hour * 60),
        }
        data.append(value)

    days_of_week = data_to_list_week(data)

    return JsonResponse(data={"data": days_of_week})


def time_count_month(request):
    data = []
    today = datetime.now().day
    times = Time.objects.filter(date__month=datetime.now().month)

    for time in times:
        day = int(time.date.strftime("%d"))
        count = 0
        if day <= today:
            count = time.minute + (time.hour * 60)
        value = {
            "day": day,
            "count": count,
        }
        data.append(value)

    days_of_month = data_to_list_month(data)[1]
    labels = data_to_list_month(data)[0]

    return JsonResponse(data={"data": days_of_month, "labels": labels})


def time_chart_of_week(request):
    context = {
        "date": datetime.now().strftime("%d %B %Y %A")
    }
    return render(request, "chart/time_chart_of_week.html", context)


def time_chart_of_month(request):
    context = {
        "date": datetime.now().strftime("%d %B %Y %A")
    }
    return render(request, "chart/time_chart_of_month.html", context)
