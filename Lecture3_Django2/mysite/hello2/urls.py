from django.urls import path

# . meaning in the direct directory 
from . import views

urlpatterns = [
    # "" means nothing to declare for the default route when the url is visited
    # view.index means what view should be rendered, when the url is visited 
    # name for giving a name to the particular url pattern, make it easy to reference form another parts of the application
    path("", views.index, name="index"),
    path("brian", views.brian, name="brian"),
    path("<str:name>", views.greet, name="greet"),
]