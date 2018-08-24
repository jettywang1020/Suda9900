from django.urls import path, re_path
from django.views.generic.base import TemplateView

from . import views


app_name = 'public'

urlpatterns = [
	path('index', views.index, name='index'),
	path('Home', views.Home, name='Home'),
	path('Register', views.Register, name='Register'),
	path('View_Detail',views.View_Detail, name= 'View_Detail')
]