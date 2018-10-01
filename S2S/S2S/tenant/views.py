from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from public.models import User, House

# Create your views here.
def index(request):
	# tenant = Tenant.objects.get(pk = 1)
	return render(request, 'tenant/index.html', locals())

def test(request):
	test_id = request.GET.get("test_id")
	data = {"test_id":test_id}
	return JsonResponse(data)

def help(request):
	return render(request, 'tenant/help.html')

def history(request):
	return render(request,'tenant/history.html')

def add_comm(request):
	return render(request,'tenant/add_comm.html')