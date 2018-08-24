from django.urls import path, re_path
from django.views.generic.base import TemplateView

from . import views


app_name = 'public'

urlpatterns = [
	path('login', views.login, name='login'),
	path('signup', views.signup, name='signup'),
	
	path('Home', views.test, name='Home'),
	path('Display', views.Display, name='Display'),
]