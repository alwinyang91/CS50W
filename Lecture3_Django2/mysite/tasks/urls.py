from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("index2", views.index2, name="index2"),
    path("add2", views.add2, name="add2"),
]