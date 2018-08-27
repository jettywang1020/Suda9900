from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
	hello = 'hello, everyone'
	return render(request, 'public/index.html', {'hello': hello})

def test(request):
	return render(request, 'public/Home.html')


def get_data(request):
	tenantList = Tenant.objects.all()
	tenants = {'list_tenant': tenantList}
	return render(request,'public/get_data.html',tenants)



