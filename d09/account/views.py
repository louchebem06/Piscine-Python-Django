from django.shortcuts import render
from django.contrib import auth
from django.http import Http404, HttpResponse
import json

# Create your views here.
def login(request):
	return render(request, "account/index.html", {})

def ajax_login(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			data = json.dumps({ 'success' : "Logged as " + username })
			return HttpResponse(data, content_type="application/json")
		else:
			data = json.dumps({ 'error' : "User or Password is invalid!" })
			return HttpResponse(data, content_type="application/json")
	else:
		raise Http404

def ajax_logout(request):
	if request.method == "POST":
		auth.logout(request)
		return HttpResponse(json.dumps({"success":"logout"}), content_type="application/json")
	else:
		raise Http404
