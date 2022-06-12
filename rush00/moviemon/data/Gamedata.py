from .Memory import Memory
from .Omdb import Omdb
import random

class Gamedata:
	def __init__(self):
		self.vector = None
		self.movieball = None
		self.moviedex = None
		self.slot = None

	def load(self, slotLetter):
		mem = Memory()

		slot = mem.load(slotLetter)
		if slot:
			self.slot = slot
			self.vector = slot['vector']
			self.movieball = slot['movieball']
			self.moviedex = slot['moviedex']
			return self
		return None

	def dump(self):
		return self.slot

	def get_random_movie(self):
		movies = Omdb().movies
		rand = random.randrange(0, len(movies))
		i = 0
		for movie in movies:
			if i == rand:
				return movie
			i += 1

	def load_default_settings(self):
		self.vector = {'x': 1, 'y': 2, 'z': 0}
		self.movieball = 10
		self.moviedex = []
		return self

	def get_strength(self):
		mem = Memory()
		current = mem.load('current')
		if current == None:
			return 0
		return len(current["moviedex"]) / len(Omdb().movies) * 10

	def get_movie(self, name):
		movies = Omdb().movies
		for movie in movies:
			if name == movie["Title"]:
				return movie
		return None
