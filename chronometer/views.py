from django.shortcuts import render, redirect, HttpResponseRedirect
from questionTracker.models import Area, Lesson
from .models import Chronometer
from datetime import datetime

def timer(request):
    now_day = datetime.now().day
    now_month = datetime.now().month

    areas = Area.objects.all()
    lessons = Lesson.objects.all()

    chronometers = Chronometer.objects.filter(date__day=now_day, date__month= now_month).order_by("-date")

    context = {
        "areas": areas,
        "lessons": lessons,
        "chronometers": chronometers
    }
    return render(request, "chronometer/timer.html", context = context)

def chronometer(request):
    now_day = datetime.now().day
    now_month = datetime.now().month

    chronometers = Chronometer.objects.filter(date__day=now_day, date__month= now_month).order_by("-date")
    
    areas = Area.objects.all()
    lessons = Lesson.objects.all()

    context = {
        "areas": areas,
        "lessons": lessons,
        "chronometers": chronometers
    }
    return render(request, "chronometer/index.html", context = context)
    
   
def save_chronometer(request):
    chronometers = Chronometer.objects.all()
    if request.method == "POST":
        area = request.POST["area"]
        lesson = request.POST["lesson"]
        count = request.POST["count"]
        true = request.POST["true"]
        false = request.POST["false"]

        chronometer = Chronometer()
        chronometer.area_id = area
        chronometer.lesson_id = lesson
        chronometer.question = count
        chronometer.true = true
        chronometer.false = false

        chronometer.name = request.POST["name"]
        chronometer.date = datetime.now()
        
        minute = request.POST["minute"]
        if minute == "" or minute == None: chronometer.minute = 0
        else: chronometer.minute = minute
        
        second = request.POST["second"]
        if second == "" or second == None: chronometer.second =  0
        else: chronometer.second = second
        
        chronometer.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    context = {
        "areas": Area.objects.all(),
        "lessons": Lesson.objects.all(),
    }

    return redirect("chronometerIndex")