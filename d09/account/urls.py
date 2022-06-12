from django.urls import path
from . import views

urlpatterns = [
	path('', views.login),
	path('ajax/login', views.ajax_login),
	path('ajax/logout', views.ajax_logout),
]