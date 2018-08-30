from django.urls import path, re_path
from django.views.generic.base import TemplateView

from . import views


app_name = 'public'

urlpatterns = [
	path('index', views.index, name='index'),
	path('login', views.login, name='login'),
	path('logout', views.logout, name='logout'),
	path('signup', views.signup, name='signup'),
	path('search', views.search, name='search'),
	path('display', views.display, name='display'),
	path('view_detail/<int:id>', views.view_detail, name='view_detail'),
	path('profile', views.profile, name='profile'),
]