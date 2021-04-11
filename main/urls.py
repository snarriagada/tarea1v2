from django.urls import path

from . import views

urlpatterns = [
path("", views.home, name="home"),
path("v1/", views.v1, name="view 1"),
path("breakingbad/<int:s>/", views.breakingbad, name="breakingbad"),
path("bettercallsaul/<int:s>/", views.bettercallsaul, name="bettercallsaul"),
path("episode/<int:serie>/<int:s>/<int:e>/", views.episodios, name="episodios"),
path("character/<int:serie>/<int:s>/", views.character, name="character")


]