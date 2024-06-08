from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("withstyle", views.withstyle, name = "withstyle"),
]