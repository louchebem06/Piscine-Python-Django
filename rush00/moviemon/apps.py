from django.apps import AppConfig
from django.conf import settings
from .data.Omdb import Omdb

class MoviemonConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'moviemon'

	def __init__(self, app_name, app_module):
		super().__init__(app_name, app_module)
		self.omdb = []

	def ready(self):
		self.omdb = Omdb().movies
		try:
			if not settings.MAX_X or type(settings.MAX_X) != int:
				raise Exception('MAX_X is not int')
			elif not settings.MAX_X or type(settings.MAX_Y) != int:
				raise Exception('MAX_Y is not int')
			if settings.MAX_X < 10:
				raise Exception('MAX_X should be at least 10')
			elif settings.MAX_Y < 10:
				raise Exception('MAX_X should be at least 10')
			if not settings.MOVIES or type(settings.MOVIES) != list:
				raise Exception('MOVIES is not a list')
			elif len(settings.MOVIES) < 10:
				raise Exception('MOVIES should be at least 10 movies')
			if not settings.OMDB_API or type(settings.OMDB_API) != str:
				raise Exception('OMDB_API is not valid')
		except Exception as e:
			print('Please use correct setting!', e)
			exit()
