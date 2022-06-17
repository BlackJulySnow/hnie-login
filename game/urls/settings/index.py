from django.urls import path
from game.views.settings.signin import signin
from game.views.settings.getStatus import getStatus
from game.views.settings.getYzm import getYzm
from game.views.settings.JWlogin import JWlogin


urlpatterns = [
    path("signin/", signin, name="settings.signin"),
    path("getStatus/", getStatus, name="settings.getStatus"),
    path("getYzm/", getYzm, name="settings.getYzm"),
    path("JWlogin/", JWlogin, name="settings.JWlogin"),
]
