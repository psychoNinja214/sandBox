from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'sandy/home.html')


def music(request):
    return render(request, 'sandy/music.html')

def video(request):
    return render(request, 'sandy/video.html')

def gallery(request):
    return render(request, 'sandy/gallery.html')

def literature(request):
    return render(request, 'sandy/literature.html')