from django.shortcuts import render, reverse, redirect
from .data.Omdb import Omdb
from .data.Memory import Memory
from django.conf import settings
from time import time
import random
from .data.Gamedata import Gamedata

def btn(a = None, b = None, start = None, select = None,
			top = None, bottom = None, left = None, right = None):
	return {
		'a': a,
		'b': b,
		'start': start,
		'select': select,
		'top': top,
		'bottom': bottom,
		'left': left,
		'right': right,
	}

def titlescreen(request):
	context = {
		'title' : 'Titlescreen',
		'btn': btn(a = reverse('worldmap') + '?newgame=1',
				   b = reverse('load_game')),
	}
	return render(request, 'moviemon/titlescreen.html', context)

def findMovie(lmovie, movies):
	for movie in movies:
		if movie["imdbID"] == lmovie["imdbID"]:
			return True
	return False

def worldmap(request):
	mem = Memory()

	if request.GET.get('newgame'):
		mem.new_game()
		return redirect('worldmap')
	
	current = mem.load('current')
	if current == None:
		return redirect('titlescreen')

	if request.GET.get('vx') or request.GET.get('vy'):
		vx = (request.GET.get('vx') == 'r' and 1) or -1
		vy = (request.GET.get('vy') == 'b' and 1) or -1

		MAX_X = settings.MAX_X
		MAX_Y = settings.MAX_Y
		prev_x = current['vector']['x']
		prev_y = current['vector']['y']
		if request.GET.get('vx'):
			current['vector']['x'] = min(max(current['vector']['x'] + vx, 0), MAX_X - 1)
		else:
			current['vector']['y'] = min(max(current['vector']['y'] + vy, 0), MAX_Y - 1)
		x = current['vector']['x']
		y = current['vector']['y']
		if prev_x != x or prev_y != y:
			current['vector']['z'] = int(time() * 1000000 + x + y)

		mem.save(current['vector'], current['movieball'], current['moviedex'], 'current')
		return redirect('worldmap')

	if 'z' not in current['vector']:
		print('default z :/')
		current['vector']['z'] = 0

	x = current['vector']['x']
	y = current['vector']['y']
	z = current['vector']['z']

	random.seed(int(z))
	rand = random.random()
	lootSomething = False
	flushedout = False
	if rand >= 0.8:
		flushedout = True
	elif rand < 0.1 or (y == 6 and x == 2 and rand < 0.45):
		lootSomething = True
		current['movieball'] += 1
		mem.save(current['vector'], current['movieball'], current['moviedex'], 'current')

	context = {
		'title' : 'Worldmap',
		'btn': btn(a = reverse('worldmap'),
				   top = reverse('worldmap') + '?vy=t',
				   bottom = reverse('worldmap') + '?vy=b',
				   left = reverse('worldmap') + '?vx=l',
				   right = reverse('worldmap') + '?vx=r',
				   start = reverse('options'),
				   select = reverse('moviedex')),
		'playerX': current['vector']['x'],
		'playerY': current['vector']['y'],
		'playerZ': current['vector']['z'],
		'MAX_X': settings.MAX_X,
		'MAX_Y': settings.MAX_Y,
		'rangeX': range(settings.MAX_X),
		'rangeY': range(settings.MAX_Y),
		'height_td': 100/settings.MAX_Y,
		'movieball': current['movieball'],
		'flushedout': flushedout, # <-- TODO: apparition d'un Moviemon
		'lootSomething': lootSomething
	}

	if flushedout:
		unknow = []
		movies = Omdb().movies
		for movie in movies:
			if not findMovie(movie, current['moviedex']):
				unknow.append(movie)
		if len(unknow) > 0:
			index = int(z) % (len(unknow) or 1)
			ttid = unknow[index]["imdbID"]
			context['btn']['a'] = reverse("battle", args=(ttid,))
		else:
			context['btn']['a'] = '#'
			context['flushedout'] = False

	if x == 0:
		context['btn']['left'] = '#'
	elif x == settings.MAX_X - 1:
		context['btn']['right'] = '#'
	if y == 0:
		context['btn']['top'] = '#'
	elif y == settings.MAX_Y - 1:
		context['btn']['bottom'] = '#'
	return render(request, 'moviemon/worldmap.html', context)

def battle(request, moviemon_id):
	mem = Memory()

	current = mem.load('current')
	if current == None:
		return redirect('titlescreen')

	cheating = False
	try:
		# antitriche
		cheating = True
		if 'z' not in current['vector']:
			print('default z :/')
			current['vector']['z'] = 0

		z = current['vector']['z']

		random.seed(int(z))
		rand = random.random()
		if rand >= 0.8:
			unknow = []
			movies = Omdb().movies
			for movie in movies:
				if not findMovie(movie, current['moviedex']):
					unknow.append(movie)
			if len(unknow) > 0:
				index = int(z) % (len(unknow) or 1)
				ttid = unknow[index]["imdbID"]
				if ttid == moviemon_id:
					cheating = False
				else:
					print('mauvaise id', ttid, moviemon_id)
		else:
			print('aucun combat?', rand)
	except:
		cheating = False

	if cheating:
		print('triche')
		return redirect('worldmap')

	captured = False
	for monster in current["moviedex"]:
		if monster["imdbID"] == moviemon_id:
			captured = True
	monster = next(monster for monster in Omdb().movies if monster["imdbID"] == moviemon_id)
	me = Gamedata().get_strength() * 5
	monsterStrenght = float(monster["imdbRating"]) * 10
	c = 50 - monsterStrenght + me
	if c <= 1:
		c = 1
	elif c >= 90:
		c = 90
	random.seed(int(time() * 1000000))
	a = random.randrange(0, 100)
	if not request.GET.get('click'):
		message = "A " + monster["Title"] + " wild appears!"
	elif current['movieball'] >= 1 and not captured:
		current['movieball'] -= 1
		mem.save(current['vector'], current['movieball'], current['moviedex'], 'current')
		if a < c:
			message = "You caught it"
			captured = True
			current["moviedex"].append(monster)
			mem.save(current['vector'], current['movieball'], current['moviedex'], 'current')
		else:
			message = "You missed !"
	elif captured:
		message = "You caught it"
	else:
		message = "You don't have any movieball !"
	context = {
		'title' : 'Battle - ' + str(monster["Title"]),
		'monster' : monster,
		'btn': btn(a = reverse('battle', args=(moviemon_id,)) + '?click=True',
				   b = reverse("worldmap")),
		'message' : message,
		'movieball' : current['movieball'],
		'captured': captured,
		'strength' : Gamedata().get_strength(),
		'chance' : c
	}
	if captured or current['movieball'] < 1:
		context['btn']['a'] = '#'
	return render(request, 'moviemon/battle.html', context)

def moviedex(request):
	mem = Memory()

	current = mem.load('current')
	if current == None:
		return redirect('titlescreen')

	dex = current['moviedex']
	select = getSelect(request, len(dex))
	idMonster = str(0)
	i = 0
	for monster in dex:
		if str(i) == str(select):
			idMonster = monster["imdbID"]
		i += 1
	context = {
		'btn': btn(a = reverse("moviedexItem", args=(idMonster,)),
				   select = reverse('worldmap'),
				   top = reverse('moviedex') + '?select=' + str(max(select - 1, 0)) + "#focus_monster",
				   bottom = reverse('moviedex') + '?select=' + str(min(select + 1, len(dex) - 1))  + "#focus_monster"),
		'select': select + 1,
		'title' : 'MovieDex',
  		"monsters" : dex
	}
	if select == 0:
		context['btn']['top'] = '#focus_monster'
	elif select == len(dex) - 1:
		context['btn']['bottom'] = '#focus_monster'
	return render(request, 'moviemon/moviedex.html', context)

def moviedexItem(request, moviemon = None):
	dex = Omdb().movies
	if not moviemon == None:
		try:
			monster = next(monster for monster in dex if monster["imdbID"] == moviemon)
			name = monster["Title"]
			poster = monster["Poster"]
			score = monster["imdbRating"]
			director = monster["Director"]
			years = monster["Year"]
			synopsis = monster["Plot"]
			actors = monster["Actors"]
		except:
			return redirect("moviedex")
	context = {
		'btn': btn(a = None,
				   b = reverse('moviedex'),
				   top = None,
				   bottom = None),
		"name": name,
		"poster" : poster,
		"score" : score,
		"director" : director,
		"years": years,
		"synopsis" : synopsis,
		"actors": actors,
	   	'title' : 'MovieDex | ' + name
	}
	return render(request, 'moviemon/moviedexItem.html', context)

def getSelect(request, maxValue = 2):
	select = request.GET.get('select')
	if not select or not select.isdigit():
		select = 0
	return max(min(int(select), maxValue), 0)

def load_game(request):
	mem = Memory()

	select = getSelect(request)
	# Current slot state:
	currentSlotLetter = ('A', 'B', 'C')[select]
	select_isLoaded = mem.currentstate_is_slot(currentSlotLetter)
	current_page = reverse('load_game') + '?select=' + str(select)
	if request.GET.get('loadslot'):
		if (request.GET.get('loadslot') == request.GET.get('select')):
			print('load', currentSlotLetter)
			mem.load_slot(currentSlotLetter)
		return redirect(current_page)

	# btn.a
	btnA = None
	if not mem.check_slot(currentSlotLetter):
		pass
	elif not select_isLoaded:
		btnA = current_page + '&loadslot=' + str(select)
	else:
		btnA = reverse('worldmap')
	context = {
		'title' : 'Load game',
		'btn': btn(a = btnA,
				   b = reverse('titlescreen'),
				   top = reverse('load_game') + '?select=' + str(max(select - 1, 0)),
				   bottom = reverse('load_game') + '?select=' + str(min(select + 1, 2))),
		'score': {
			'a': mem.check_slot('A'),
			'b': mem.check_slot('B'),
			'c': mem.check_slot('C')
		},
		'select': select,
		'select_isLoaded': select_isLoaded
	}
	if select == 0:
		context['btn']['top'] = '#'
	if select == 2:
		context['btn']['bottom'] = '#'
	return render(request, 'moviemon/load_game.html', context)

def save_game(request):
	mem = Memory()

	current = mem.load('current')
	if current == None:
		return redirect('titlescreen')

	select = getSelect(request)
	# Current slot state:
	currentSlotLetter = ('A', 'B', 'C')[select]
	current_page = reverse('save_game') + '?select=' + str(select)
	if request.GET.get('savegame'):
		if (request.GET.get('savegame') == request.GET.get('select')):
			print('save', currentSlotLetter)
			mem.save(current['vector'], current['movieball'], current['moviedex'], currentSlotLetter)
		return redirect(current_page)

	context = {
		'title' : 'Save game',
		'btn': btn(a = reverse('save_game') + '?select=' + str(select) + '&savegame=' + str(select),
				   b = reverse('options'),
				   top = reverse('save_game') + '?select=' + str(max(select - 1, 0)),
				   bottom = reverse('save_game') + '?select=' + str(min(select + 1, 2))),
		'score': {
			'a': mem.check_slot('A'),
			'b': mem.check_slot('B'),
			'c': mem.check_slot('C')
		},
		'select': select,
	}
	if select == 0:
		context['btn']['top'] = '#'
	if select == 2:
		context['btn']['bottom'] = '#'
	return render(request, 'moviemon/save_game.html', context)

def options(request):
	context = {
		'title' : 'Options',
		'btn': btn(a = reverse('save_game') ,
				   b = reverse('titlescreen'),
				   start = reverse('worldmap'))
	}
	return render(request, 'moviemon/options.html', context)
