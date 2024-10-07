from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Name the path "index"
]
