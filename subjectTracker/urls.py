from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="subjectTrackerIndex"),
    path(
        "change-status-subject/<int:id>",
        views.change_status_subject,
        name="changeStatusSubject",
    ),
    path("delete-subject/<int:id>", views.delete_subject, name="deleteSubject"),
    path("back-to-subject", views.back_to_subject, name="backToSubject"),
    path("filter-subject", views.filter_subject, name="filterSubject"),
]
