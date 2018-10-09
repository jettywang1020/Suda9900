from django.urls import path, re_path
from django.views.generic.base import TemplateView

from . import views


app_name = 'tenant'

urlpatterns = [
	path('', views.index, name='index'),
	path('test/', views.test, name='test'),
	path('help/', views.help, name='help'),
	path('history/', views.history, name='history'),
	path('add_comm/<int:id>', views.add_comm,name='add_comm'),
	path('house_list',views.house_list, name ="house_list"),
	path('post',views.post, name= "post"),
	path('house_detail',views.house_detail, name ="house_detail"),
]