from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
from django.conf import settings

def init(request):
	db = settings.DATABASES['default']
	try:
		conn = psycopg2.connect(
			database = db["NAME"],
			host = db["HOST"],
			user = db["USER"],
			password = db["PASSWORD"],
		)
		curr = conn.cursor()
		curr.execute("""CREATE TABLE IF NOT EXISTS ex04_movies (
			episode_nb serial,
			PRIMARY KEY(episode_nb),
			title varchar(64) NOT NULL UNIQUE,
			opening_crawl text,
			director varchar(32) NOT NULL,
			producer varchar(128) NOT NULL,
			release_date date
		)
		""")
		conn.commit()
		conn.close()
	except Exception as e:
		return HttpResponse(e)
	return HttpResponse("OK")

def populate(request):
	db = settings.DATABASES['default']
	datas = [
		(1, "The Phantom Menace", None, "George Lucas", "Rick McCallum", "1999-05-19"),
		(2, "Attack of the Clones", None, "George Lucas", "Rick McCallum", "2002-05-16"),
		(3, "Revenge of the Sith", None, "George Lucas", "Rick McCallum", "2005-05-19"),
		(4, "A New Hope", None, "George Lucas", "GaryKurtz, Rick McCallum", "1977-05-25"),
		(5, "The Empire Strikes Back", None, "Irvin Kershner", "GaryKurtz, Rick McCallum", "1980-05-17"),
		(6, "Return of the Jedi", None, "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", "1983-05-25"),
		(7, "The Force Awakens", None, "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "2015-12-11"),
	]
	value = list()
	try:
		conn = psycopg2.connect(
			database = db["NAME"],
			host = db["HOST"],
			user = db["USER"],
			password = db["PASSWORD"],
		)
		curr = conn.cursor()
		for data in datas:
			try:
				curr.execute("INSERT INTO ex04_movies (episode_nb, title, opening_crawl, director, producer, release_date) VALUES(%s, %s, %s, %s, %s, %s)", data)
				value.append("<p>OK</p>")
			except Exception as e:
				value.append("<p>" + str(e) + "</p>")
			conn.commit()
		conn.close()
	except Exception as e:
		return HttpResponse(e)
	return HttpResponse(value)

def display(request):
	db = settings.DATABASES['default']
	try:
		conn = psycopg2.connect(
			database = db["NAME"],
			host = db["HOST"],
			user = db["USER"],
			password = db["PASSWORD"],
		)
		curr = conn.cursor()
		curr.execute("SELECT * FROM ex04_movies")
		values = curr.fetchall()
		conn.close()
	except Exception as e:
		return HttpResponse("No data available")
	if len(values) == 0:
		return HttpResponse("No data available")
	return render(request, "ex04/display.html", {"values" : values})

def remove(request):
	db = settings.DATABASES['default']
	conn = psycopg2.connect(
		database = db["NAME"],
		host = db["HOST"],
		user = db["USER"],
		password = db["PASSWORD"],
	)
	curr = conn.cursor()
	if request.method == "POST":
		value = request.POST.get("movie_form")
		if not value == None:
			curr.execute("DELETE FROM ex04_movies WHERE episode_nb = %s", value)
			conn.commit()
	curr.execute("SELECT * FROM ex04_movies")
	values = curr.fetchall()
	conn.close()
	return render(request, "ex04/remove.html", {"values" : values})