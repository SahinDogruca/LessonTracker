from django.urls import path
from . import views

urlpatterns = [
    # question charts
    path(
        "question-chart-of-week",
        views.question_chart_of_week,
        name="questionChartOfWeek",
    ),
    path("question-count-week/", views.question_count_week, name="questionCountWeek"),
    path(
        "question-chart-of-month",
        views.question_chart_of_month,
        name="questionChartOfMonth",
    ),
    path(
        "question-count-month/", views.question_count_month, name="questionCountMonth"
    ),
    # time charts
    path("time-count-week", views.time_count_week, name="timeCountWeek"),
    path("time-count-month", views.time_count_month, name="timeCountMonth"),
    path("time-chart-of-week", views.time_chart_of_week, name="timeChartOfWeek"),
    path("time-chart-of-month", views.time_chart_of_month, name="timeChartOfMonth"),
]
