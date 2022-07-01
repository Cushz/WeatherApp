from nturl2path import url2pathname
from django.urls import path
from .views import *
urlpatterns = [
    path("",indexView,name="index"),
]
