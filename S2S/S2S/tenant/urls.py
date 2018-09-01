from django.urls import path, re_path
from django.views.generic.base import TemplateView

from . import views


app_name = 'tenant'

urlpatterns = [
	path('', views.index, name='index'),
	path('test/', views.test, name='test'),
	path('booking/', views.booking, name='booking'),
]