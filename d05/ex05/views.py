from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies

# Create your views here.
def populate(request):
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
	for data in datas:
		try:
			Movies.objects.create(
				episode_nb = data[0],
				title = data[1],
				opening_crawl = data[2],
				director = data[3],
				producer = data[4],
				release_date = data[5]
			)
			value.append(str("<p>OK</p>"))
		except Exception as e:
			value.append(str("<p>" + str(e) + "</p>"))
	return HttpResponse(value)

def display(request):
	try:
		m = Movies.objects.all()
		if len(m.values_list()) == 0:
			return HttpResponse("No data available")
		return render(request, "ex05/display.html", {"values" : m.values_list()})
	except Exception as e:
		return HttpResponse("No data available")

def remove(request):
	if request.method == "POST":
		value = request.POST.get("movie_form")
		if not value == None:
			rm = Movies.objects.get(episode_nb=value)
			rm.delete()
	m = Movies.objects.all()
	return render(request, "ex05/remove.html", {"values" : m.values_list()})