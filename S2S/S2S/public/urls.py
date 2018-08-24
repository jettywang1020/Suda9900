from django.urls import path, re_path
from django.views.generic.base import TemplateView

from . import views


app_name = 'public'

urlpatterns = [
	path('login', views.login, name='login'),	# login page
	path('index', views.index, name='index'),	# login page raw

	path('signup', views.signup, name='signup'),	# signup page
	path('Register', views.Register, name='Register'),	# signup page raw
	
	path('Home', views.Home, name='Home'),	# search house page
	path('Display', views.Display, name='Display'),	# row houses page
	path('View_Detail',views.View_Detail, name= 'View_Detail'),	# house detial page
]