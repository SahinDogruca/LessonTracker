"""LessonTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin", admin.site.urls),
    path("question-tracker/", include("questionTracker.urls")),
    path("", include("home.urls")),
    path("todo/", include("todo.urls")),
    path("charts/", include("chart.urls")),
    path("time-tracker/", include("timeTracker.urls")),
    path("subject-tracker/", include("subjectTracker.urls")),
    path("test-tracker/", include("testTracker.urls")),
    path("chronometer/", include("chronometer.urls")),
    path('gallery/', include('photos.urls')),

]


handler404 = "home.views.page_not_found"

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)