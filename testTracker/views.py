from django.shortcuts import render
from .models import BranchTest, AreaTest
from questionTracker.models import Lesson


def branch_test(request):
    context = {
        "tests": BranchTest.objects.filter(area_test__isnull=True).order_by("-date"),
        "lessons": Lesson.objects.all(),
    }
    return render(request, "testTracker/branch_test.html", context)


def area_test_ayt(request):
    area_test = AreaTest.objects.filter(area_id=2).order_by("-date")
    branch_test = BranchTest.objects.filter(area_test__in=area_test)

    context = {
        "area_tests": area_test,
        "branch_tests": branch_test,
    }
    return render(request, "testTracker/area_test_ayt.html", context)


def area_test_tyt(request):
    area_test = AreaTest.objects.filter(area_id=1).order_by("-date")
    branch_test = BranchTest.objects.filter(area_test__in=area_test)

    context = {
        "area_tests": area_test,
        "branch_tests": branch_test,
    }
    return render(request, "testTracker/area_test.html", context)


def filter_test_branch(request):
    tests = BranchTest.objects.filter(area_test__isnull=True)
    if request.method == "POST":
        lesson = request.POST["lesson"]
        if lesson == "empty":
            tests = BranchTest.objects.all()
        else:
            tests = BranchTest.objects.filter(lesson_id=lesson, area_test__isnull=True)

    context = {
        "tests": tests,
        "lessons": Lesson.objects.all(),
    }

    return render(request, "testTracker/branch_test.html", context)


def calc_score(request):
    return render(request, "testTracker/calc_score.html")

