from django.urls import path
from . import views

urlpatterns = [
    path('', views.colors, name='index'),
]