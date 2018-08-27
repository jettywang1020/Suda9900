from django.urls import path, re_path
from django.views.generic.base import TemplateView

from . import views


app_name = 'public'

urlpatterns = [
<<<<<<< HEAD


	path('index', views.index, name='index'),
	path('search', views.search, name='search'),
	path('Register', views.Register, name='Register'),
	path('view_detail',views.view_detail, name= 'view_detail'),

	path('login', views.login, name='login'),
	path('signup', views.signup, name='signup'),
	

	path('Display', views.Display, name='Display'),


=======
>>>>>>> 8a7ef0ddcfdcd993899de0cf0cefa488821120e6
	path('login', views.login, name='login'),	# login page
	path('logout', views.logout, name='logout'),	# logout page
	path('signup', views.signup, name='signup'),	# signup page
	
<<<<<<< HEAD
	path('Home', views.Home, name='Home'),	# search house page
	path('Display', views.Display, name='Display'),	# row houses page
	path('View_Detail',views.View_Detail, name= 'View_Detail'),	# house detial page

=======
	path('search', views.search, name='search'),	# search house page
	path('display', views.display, name='display'),	# row houses page
	path('view_detail', views.view_detail, name='view_detail'),	# house detial page

	path('index', views.index, name='index'),	# personal navs page
	path('profile', views.profile, name='profile'),	# personal profile page
	
>>>>>>> 8a7ef0ddcfdcd993899de0cf0cefa488821120e6
]