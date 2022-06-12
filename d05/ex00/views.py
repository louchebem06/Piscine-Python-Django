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
		curr.execute("""CREATE TABLE IF NOT EXISTS ex00_movies (
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
