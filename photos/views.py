from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Photo, Status
from .filters import PhotoFilter
from questionTracker.models import *
from django.core.paginator import Paginator
import string

# Create your views here.

def gallery(request):
    url = request.META["HTTP_REFERER"]
    
    photos = Photo.objects.all().order_by("-date")
    photo_length = len(photos)
    photoFilter = PhotoFilter(request.GET, queryset=photos)
    photos = photoFilter.qs

    photo_paginator = Paginator(photos, 30)


    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        page = photo_paginator.page(page)
    except:
        page = photo_paginator.page(1)

    

    index = page.number - 1

    max_index = len(photo_paginator.page_range)

    start_index = index - 1 if index >= 1 else 0
    end_index = index + 2 if index <= max_index - 2 else max_index

    page_range = list(photo_paginator.page_range)[start_index:end_index]


    str_url = request.get_full_path()
    cleaned_str_url = str_url.rstrip(string.digits)
    url = cleaned_str_url.rstrip("&page=")
    
    # bişey status'daki =(num) 'ı siliyor



    context = {
        'page': page,
        'photofilter':photoFilter.form, 
        "lessons": Lesson.objects.all(), 
        "areas": Area.objects.all(), 
        "statues": Status.objects.all(),
        "page_range": page_range,
        "url": url,
        "photo_length": photo_length
    }
    return render(request, 'photos/gallery.html', context)


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    status = True
    return render(request, 'photos/photo.html', {'photo': photo})

def editPhoto(request, id):
    photo = Photo.objects.get(id=id)

    area = Area.objects.all()
    lesson = Lesson.objects.all()


    if request.method == 'POST':
        data = request.POST

        if data['area'] != 'none':
            area = Area.objects.get(id=data['area'])
        else:
            area = None
        
        if data['lesson'] != 'none':
            lesson = Lesson.objects.get(id=data['lesson'])
        else:
            lesson = None
        
        if data['status'] != 'none':
            status = Status.objects.get(id=data['status'])
        else:
            status = None
        
        photo.title = data["title"]
        photo.description = data["description"]
        photo.area = area
        photo.lesson = lesson
        photo.status = status


        photo.save()

        return redirect("gallery")

    context = {"areas":area, "lessons":lesson, "statues": Status.objects.all(), "photo":photo}
    return render(request, "photos/edit.html", context)



def addPhoto(request):
    area = Area.objects.all()
    lesson = Lesson.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')


        if data['area'] != 'none':
            area = Area.objects.get(id=data['area'])
        else:
            area = None
        
        if data['lesson'] != 'none':
            lesson = Lesson.objects.get(id=data['lesson'])
        else:
            lesson = None
        
        if data['status'] != 'none':
            status = Status.objects.get(id=data['status'])
        else:
            status = None


        for image in images:
            photo = Photo.objects.create(
                area=area,
                lesson=lesson,
                title=data["title"],
                status=status,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')


    context = {"areas":area, "lessons":lesson, "statues": Status.objects.all()}
    return render(request, 'photos/add.html', context)