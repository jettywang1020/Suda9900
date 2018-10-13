from django.urls import path, re_path
from django.views.generic.base import TemplateView

from . import views


app_name = 'tenant'

urlpatterns = [
	path('help/', views.help, name='help'),
	path('history/', views.history, name='history'),
	path('add_comm/<int:id>', views.add_comm,name='add_comm'),
	path('post_list',views.post_list, name ="post_list"),
	path('post',views.post, name= "post"),
	path('post_detail/<int:id>',views.post_detail, name ="post_detail"),
	path('apply',views.apply,name='apply'),
]