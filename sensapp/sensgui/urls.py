from django.conf.urls import *
from django.contrib import admin
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
url(r'^', views.login , name='login'),
]
urlpatterns += staticfiles_urlpatterns()