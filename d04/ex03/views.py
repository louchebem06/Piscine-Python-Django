from django.shortcuts import render

# Create your views here.
def colors(request):
	color = list()
	color.append("0")
	color.append("1")
	color.append("2")
	color.append("3")
	color.append("0")
	color.append("1")
	color.append("2")
	color.append("3")
	color.append("0")
	color.append("1")
	color.append("2")
	color.append("3")
	color.append("0")
	color.append("1")
	color.append("2")
	color.append("3")
	return render(request, "ex03/index.html", {"color" : color})