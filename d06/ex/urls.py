from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('delete_tip/<id>', views.deleteTip, name='deleteTip'),
    path('vote_tip/<id>/<state>', views.voteTip, name='voteTip')
]