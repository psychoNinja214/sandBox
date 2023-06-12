from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("music", views.music, name="music"),
    path("video", views.video, name="video"),
    path("gallery", views.gallery, name="gallery"),
    path("literature", views.literature, name="literature"),
]