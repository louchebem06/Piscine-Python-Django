from .Omdb import Omdb
import pickle5 as pickle
import os
import hashlib

def sha256sum(filename):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()

# slot<n>_<score>.mmg’.
class Memory:
	def save(self, vector: dict, movieball: int, movieDex: list, slotLetter: str):
		omdb = Omdb()
		if slotLetter == "current":
			filename = "current.mmg"
		else:
			name = self.getName_slot(slotLetter)
			if name:
				os.remove('./moviemon/data/save/' + self.getName_slot(slotLetter))
			filename = "slot" + slotLetter + "_" + str(len(movieDex)) + "_" + str(len(omdb.movies)) + ".mmg"
		file = open("./moviemon/data/save/" + filename, "wb")
		pickle.dump((vector, str(movieball), movieDex, omdb.movies), file)
		file.close()

	def load(self, slotLetter: str):
		try:
			data = list()
			if slotLetter == 'current':
				filename = 'current.mmg'
			else:
				filename = self.getName_slot(slotLetter)
			if not filename:
				return None
			with open("./moviemon/data/save/" + filename, "rb") as f:
				data += pickle.load(f)
			return {"vector":data[0],"movieball":int(data[1]),"moviedex":data[2]}
		except:
			return None

	def listSave(self):
		return os.listdir("./moviemon/data/save/")

	def currentstate_is_slot(self, slotLetter):
		try:
			filename = self.getName_slot(slotLetter)
			if not filename:
				return None
			chash = sha256sum("./moviemon/data/save/current.mmg")
			fhash = sha256sum("./moviemon/data/save/" + filename)
			print(chash, fhash)
			if chash == fhash:
				return True
		except:
			pass
		return None

	def load_slot(self, slotLetter):
		slot = self.load(slotLetter)
		if slot:
			self.save(slot['vector'], slot['movieball'], slot['moviedex'], 'current')
		return None

	def new_game(self):
		self.save({'x': 1, 'y': 2, 'z': 0}, 10, [], 'current')
		pass

	def getName_slot(self, slotLetter):
		slot = 'slot' + slotLetter.upper()
		for file in os.listdir('moviemon/data/save/'):
			if file.startswith(slot):
				return file
		return None

	def check_slot(self, slotLetter):
		file = self.getName_slot(slotLetter)
		if file:
			return file.replace('slot' + slotLetter + '_', '').replace('.mmg', '').replace('_', ' / ')
		return None