from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import RedirectView, ListView, FormView, DetailView, CreateView
from .models import Article, UserFavouriteArticle, CustomUser
from .forms import LoginForm, RegistrationForm, ArticleForm, UserFavouriteArticleForm
from django.urls import reverse, reverse_lazy
from django.contrib import auth

# Create your views here.
class Home(RedirectView):
	permanent = False
	pattern_name = 'Articles'

class ArticleList(ListView):
	model = Article
	template_name = 'ex/article_list.html'
	def get_queryset(self):
		queryset = Article.objects.filter().order_by('-created')
		return queryset
 
class Publications(ListView):
	model = Article
	template_name = 'ex/publication_list.html'
	def get_queryset(self):
		queryset = Article.objects.filter(author__username=self.request.user)
		return queryset

class Favourites(ListView):
	model = UserFavouriteArticle
	template_name = 'ex/favourite_list.html'
	def get_queryset(self):
		queryset = UserFavouriteArticle.objects.filter(user__username=self.request.user)
		return queryset

# https://stackoverflow.com/questions/6907388/updating-context-data-in-formview-form-valid-method
class Login(FormView):
	template_name = 'ex/login.html'
	form_class = LoginForm
	success_url = reverse_lazy('Home')

	def get(self, request, *args, **kwargs):
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		context = self.get_context_data(**kwargs)
		context['form'] = form
		if request.user.is_authenticated:
			return self.form_valid(form)
		return self.render_to_response(context)

	def post(self, request, *args, **kwargs):
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		if form.is_valid():
			name = form.cleaned_data['name']
			password = form.cleaned_data['password']
			user = auth.authenticate(username=name, password=password)
			if user is not None:
				auth.login(request, user)
				return self.form_valid(form)
			else:
				return self.form_invalid(form, **kwargs)

	def form_invalid(self, form, **kwargs):
		context = self.get_context_data(**kwargs)
		context['form'] = form
		context['error'] = "Username or password is invalid"
		return self.render_to_response(context)

class Logout(RedirectView):
	permanent = False
	def get_redirect_url(self):
		auth.logout(self.request)
		return reverse('Home')

class ArticleDetail(DetailView):
	model = Article
	template_name = 'ex/article_detail.html'

class Register(CreateView):
	form_class = RegistrationForm
	success_url = reverse_lazy('Home')
	template_name = 'ex/register.html'

	def get(self, request):
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		if request.user.is_authenticated:
			return HttpResponseRedirect(self.success_url)
		context = {"form" : form}
		return render(self.request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		if form.is_valid():
			try:
				name = form.cleaned_data['name']
				password = form.cleaned_data['password']
				user = CustomUser.objects.create_user(name, None, password)
				user.save()
				user = auth.authenticate(username=name, password=password)
				if user is not None:
					auth.login(request, user)
					return self.form_valid(form)
			except Exception as e:
				return self.form_invalid(form)
		context = {'form': form}
		return render(request, self.template_name, context)

	def form_invalid(self, form):
		context = dict()
		context['form'] = form
		context['error'] = "Username exist"
		return render(self.request, self.template_name, context)

class Publish(CreateView):
	form_class = ArticleForm
	success_url = reverse_lazy('Publications')
	template_name = 'ex/publish.html'

	def get(self, request):
		if not request.user.is_authenticated:
			return HttpResponseRedirect(reverse_lazy('Login'))
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		context = {"form" : form}
		return render(self.request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		if form.is_valid():
			f = form.cleaned_data
			article = Article()
			article.title = f['title']
			article.author = request.user
			article.synopsis = f['content'][:312]
			article.content = f['content']
			article.save()
			return HttpResponseRedirect(self.success_url)
		context = {'form': form}
		return render(request, self.template_name, context)

class FavouritesAdd(CreateView):
    form_class = UserFavouriteArticleForm
    success_url = reverse_lazy('Favourites')