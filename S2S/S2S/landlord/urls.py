from django.urls import path, re_path
from django.views.generic.base import TemplateView

from . import views


app_name = 'landlord'

urlpatterns = [
	path('', views.index, name='index'),
	
	path('profile', views.profile, name='profile'),
	path('add_house', views.add_house, name='add_house'),	# Landlord add house
]