from django.shortcuts import render
from django.http import HttpResponse, request
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from gallery.models import Photo, Categories

def index(request):
    photo_list = Photo.objects.all()[:12].reverse()
    categories = Categories.objects.all()
    template = loader.get_template('gallery/index.html')
    context = {
        'photo_list': photo_list,
        'categories': categories
    }
    return HttpResponse(template.render(context, request))

def category(request, album):
    photo_list = Photo.objects.filter(item_id=album).reverse()
    categories = Categories.objects.all().exclude(id = album)
    template = loader.get_template('gallery/index.html')
    context = {
        'photo_list': photo_list,
        'categories': categories
    }
    return HttpResponse(template.render(context, request))
    