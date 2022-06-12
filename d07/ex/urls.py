from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='Home'),
    path('articles', views.ArticleList.as_view(), name='Articles'),
    path('login', views.Login.as_view(), name='Login'),
    path('logout', views.Logout.as_view(), name='Logout'),
    path('detail/<int:pk>', views.ArticleDetail.as_view(), name="Detail"),
    path('publications', views.Publications.as_view(), name="Publications"),
    path('favourites', views.Favourites.as_view(), name='Favourites'),
    path('register', views.Register.as_view(), name='Register'),
    path('publish', views.Publish.as_view(), name='Publish'),
    path('add_favourites', views.FavouritesAdd.as_view(), name='Add to favourite'),
]