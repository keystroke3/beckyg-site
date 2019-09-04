from django.urls import path
from . import views

urlpatterns = [path("", views.home, name="bio-home"),
               path("about/", views.about, name="bio-about"), ]
