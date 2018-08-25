from django.urls import path, re_path
from django.views.generic.base import TemplateView

from . import views


app_name = 'public'

urlpatterns = [
	path('login', views.login, name='login'),	# login page
	path('index', views.index, name='index'),	# login page raw

	path('signup', views.signup, name='signup'),	# signup page
	path('Register', views.register, name='register'),	# signup page raw
	
	path('home', views.home, name='home'),	# search house page
	path('display', views.display, name='display'),	# row houses page
	path('view_detail',views.view_detail, name= 'view_detail'),	# house detial page
]