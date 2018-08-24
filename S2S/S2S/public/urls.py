from django.urls import path, re_path
from django.views.generic.base import TemplateView

from . import views


app_name = 'public'

urlpatterns = [
<<<<<<< HEAD
	path('index', views.index, name='index'),
	path('Home', views.Home, name='Home'),
	path('Register', views.Register, name='Register'),
	path('View_Detail',views.View_Detail, name= 'View_Detail')
=======
	path('login', views.login, name='login'),
	path('signup', views.signup, name='signup'),
	
	path('Home', views.test, name='Home'),
	path('Display', views.Display, name='Display'),
>>>>>>> 6f6fe038488bc8defdd0fb640013d263b231ad19
]