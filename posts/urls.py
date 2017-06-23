from django.conf.urls import url
from posts import  views

urlpatterns = [
    url(r'^$', views.search_form),
    url(r'^search/$', views.search),
]