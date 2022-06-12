from django import forms
from .models import Login, Registration, Article, UserFavouriteArticle

class LoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Login
		fields = [
			'name',
			'password'
		]
		widgets = {
			'password': forms.PasswordInput()
		}

class RegistrationForm(forms.ModelForm):
	class Meta:
		model = Registration
		fields = [
			'name',
			'password',
			'repassword'
		]
		widgets = {
			'password': forms.PasswordInput(),
			'repassword': forms.PasswordInput()
		}
	def clean(self):
		form_data = self.cleaned_data
		if not 'name' in form_data.keys():
			return form_data
		if not 'password' in form_data.keys():
			return form_data
		if not 'repassword' in form_data.keys():
			return form_data
		if not form_data['password'] == form_data['repassword']:
			self._errors['password'] = ["Comp error repassword"]
			self._errors['repassword'] = ["Comp error password"]
		return form_data

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = [
			'title', 'content'
		]

class UserFavouriteArticleForm(forms.ModelForm):
    class Meta:
        model = UserFavouriteArticle
        fields = [
			'user', 'article'
		]