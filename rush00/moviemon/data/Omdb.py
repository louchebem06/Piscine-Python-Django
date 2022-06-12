from django.conf import settings
import requests, json, os

class Omdb:
	movies = list()

	def get(self, id):
		url = "https://www.omdbapi.com/?i=" + id + "&apikey=" + settings.OMDB_API
		try:
			req = requests.get(url)
			if req.status_code != 200:
				raise Exception("Status code not 200 but " + req.status_code)
			return req.text
		except:
			raise Exception("Error")
	
	def __init__(self):
		if len(self.movies) == 0 and os.path.exists("./Omdb.cache") == False:
			f = open("./Omdb.cache", "a")
			for movie in settings.MOVIES:
				try:
					ret = self.get(movie)
					self.movies.append(json.loads(ret))
					f.write(ret + "\n")
				except:
					pass
			f.close()
		elif len(self.movies) == 0:
			with open("./Omdb.cache", "r") as f:
				for m in f:
					self.movies.append(json.loads(m))
