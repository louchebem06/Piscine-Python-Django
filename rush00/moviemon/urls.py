from django.urls import path

from . import views

urlpatterns = [
	path('', views.titlescreen, name='titlescreen'),
	path('worldmap', views.worldmap, name='worldmap'),
	path('battle/<moviemon_id>', views.battle, name='battle'),
	path('moviedex', views.moviedex, name='moviedex'),
	path('moviedex/<moviemon>', views.moviedexItem, name='moviedexItem'),
	path('options', views.options, name='options'),
	path('options/save_game', views.save_game, name='save_game'),
	path('options/load_game', views.load_game, name='load_game'),
]
