from django.shortcuts import render
from .form import MyForm
from django.conf import settings
from django.utils import timezone

def forms(request):
	if request.method == "POST":
		form = MyForm(request.POST)
		if form.is_valid():
			form = form.cleaned_data['text']
			f = open(settings.LOG_CHAT, "a")
			f.write(str(timezone.now()) + " : " + form + "\n")
			f.close()
	form = MyForm()
	file = list()
	try:
		with open(settings.LOG_CHAT, "r") as f:
			for l in f:
				file.append(l)
	except:
		pass
	return render(request, 'ex02/form.html',
				  {"form" : form,
				   "file" : file})