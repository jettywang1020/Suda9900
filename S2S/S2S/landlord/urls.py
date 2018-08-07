from django.urls import path, re_path
from django.views.generic.base import TemplateView

from . import views


app_name = 'landlord'

urlpatterns = [
	path('', views.index, name='index'),
]