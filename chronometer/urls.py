from django.urls import path
from . import views


urlpatterns = [
    path("chronometer", views.chronometer, name="chronometerIndex"),
    path("save-chronometer", views.save_chronometer, name="saveChronometer"),
    path("timer", views.timer, name="timerIndex"),
]

