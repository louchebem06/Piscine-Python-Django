from django.shortcuts import render, redirect
from django.conf import settings
import random
from .forms import RegistrationFrom, LoginForm, TipForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Tip, Vote

def getVote(id_tip: int) -> dict():
    id_tip = int(id_tip)
    votes = Vote.objects.filter(id_tip=id_tip)
    ret = dict()
    ret["UP"] = 0
    ret["DOWN"] = 0
    for vote in votes:
        if vote.vote == 1:
            ret['UP'] = ret['UP'] + 1
        else:
            ret['DOWN'] = ret['DOWN'] + 1
    return ret

def index(request):
	content = dict()
	content["title"] = "index"
	if request.user.is_authenticated:
		if request.method == "POST":
			form = TipForm(request.POST)
			content["form"] = form
			if form.is_valid():
				tip = Tip()
				tip.content = form.cleaned_data['content']
				tip.author = request.user.username
				tip.save()
		else:
			content["form"] = TipForm()
	tips = Tip.objects.all()
	content["tips"] = tips.values_list()
	tmp = list()
	for tip in content["tips"]:
		tip = list(tip)
		votes=getVote(tip[0])
		tip.append(votes["UP"])
		tip.append(votes["DOWN"])
		tmp.append(tip)
	content["tips"] = tmp
	if not "pseudo" in request.COOKIES.keys():
		rand = random.randint(0, 9)
		pseudo = settings.PSEUDOS[rand]
		request.COOKIES["pseudo"] = pseudo
		response = render(request, "ex/index.html", content)
		response.set_cookie("pseudo", pseudo, max_age=42)
		return response
	return render(request, "ex/index.html", content)

def registration(request):
	if request.user.is_authenticated:
		return redirect("/")
	content = dict()
	content["title"] = "registration"
	content["form"] = RegistrationFrom()
	if request.method == "POST":
		form = RegistrationFrom(request.POST)
		content["form"] = form
		if form.is_valid():
			try:
				name = form.cleaned_data['name']
				password = form.cleaned_data['password']
				user = User.objects.create_user(name, None, password)
				user.save()
				user = auth.authenticate(username=name, password=password)
				if user is not None:
					auth.login(request, user)
					return redirect("/")
			except Exception as e:
				content["error"] = "User exist"
	return render(request, "ex/form.html", content)

def login(request):
	if request.user.is_authenticated:
		return redirect("/")
	content = dict()
	content["title"] = "login"
	content["form"] = LoginForm()
	if request.method == "POST":
		form = LoginForm(request.POST)
		content["form"] = form
		if form.is_valid():
			name = form.cleaned_data['name']
			password = form.cleaned_data['password']
			user = auth.authenticate(username=name, password=password)
			if user is not None:
				auth.login(request, user)
				return redirect("/")
			else:
				content["error"] = "Password or username is not found"
	return render(request, "ex/form.html", content)

@login_required(login_url='/login')
def logout(request):
	auth.logout(request)
	return redirect("/")

@login_required(login_url='/login')
def deleteTip(request, id = None):
	if id == None or not id.isdigit():
		return redirect("/")
	id = int(id)
	try:
		tip = Tip.objects.get(id=id)
		tip.delete()
	except:
		pass
	return redirect("/")

@login_required(login_url='/login')
def voteTip(request, id = None, state = None):
	if id == None or state == None or not id.isdigit() or not state.isdigit() or int(state) >= 2:
		return redirect("/")
	id = int(id)
	state = int(state)
	try:
		username = request.user.username
		result = Vote.objects.filter(id_tip=id, username=username)
		if len(result.values_list()) == 0:
			vote = Vote()
			vote.id_tip = id
			vote.username = username
			vote.vote = state
			vote.save()
		else:
			r = result.values_list()[0]
			vote = Vote()
			vote.id = r[0]
			vote.id_tip = id
			vote.username = username
			vote.vote = r[3]
			if vote.vote == state:
				vote.delete()
			else:
				if vote.vote == 0:
					vote.vote = 1
				else:
					vote.vote = 0
				vote.save()
	except Exception as e:
		pass
	return redirect("/")
