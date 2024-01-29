from django.shortcuts import render, redirect
from .models import *
from questionTracker.views import get_date_infos


def index(request):
    context = {"times": get_times("week")}
    return render(request, "timeTracker/index.html", context)


def filter_time(request):
    times = None
    if request.method == "POST":
        date = request.POST["date"]
        if date != "":
            times = get_times(date)
        else:
            times = get_times("week")

    context = {"times": times}

    return render(request, "timeTracker/index.html", context)


def get_times(date_info):
    info = get_date_infos()

    result_info = info.get(date_info)
    month = info.get("month")

    if date_info == "year":
        times = Time.objects.filter(date__year=result_info)
    elif date_info == "month":
        times = Time.objects.filter(date__month=result_info)
    elif date_info == "week":
        times = Time.objects.filter(date__week=result_info)
    elif date_info == "day":
        times = Time.objects.filter(date__day=result_info, date__month=month)

    return times


def delete_time(request, id):
    Time.objects.get(pk=id).delete()
    return redirect("timeTrackerIndex")


def back_to_time(request):
    return redirect("timeTrackerIndex")


def add_time(request):
    if request.method == "POST":
        time = Time()
        time.title = request.POST["title"]
        hour = request.POST["hour"]
        if hour == "" or hour == None: time.hour =  0
        else: time.hour = hour
        
        minute = request.POST["minute"]
        if minute == "" or minute == None: time.minute = 0
        else: time.minute = minute
        
        time.save()
        return redirect("timeTrackerIndex")
    return render(request, "timeTracker/add_time.html")


def edit_time(request, id):
    time = Time.objects.get(pk=id)
    if request.method == "POST":
        time.title = request.POST["title"]
        hour = request.POST["hour"]
        if hour == "" or hour == None: time.hour =  0
        else: time.hour = hour
        
        minute = request.POST["minute"]
        if minute == "" or minute == None: time.minute = 0
        else: time.minute = minute
        time.save()

        return redirect("timeTrackerIndex")

    context = {
        "time": time,
    }

    return render(request, "timeTracker/edit_time.html", context)
