from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from public.models import Tenant, Landlord, House

# Create your views here.
def index(request):
	tenant = Tenant.objects.get(pk = 1)
	return render(request, 'tenant/index.html', locals())

def test(request):
	test_id = request.GET.get("test_id")
	data = {"test_id":test_id}
	return JsonResponse(data)