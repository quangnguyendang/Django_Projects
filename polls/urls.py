from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.welcome, name="welcome_site"),
    url(r'^welcome/$', views.welcome, name="welcome_site")
]
