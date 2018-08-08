from django.shortcuts import render
from public.models import Tenant, Landlord, House

# Create your views here.
def index(request):
	tenant = Tenant.objects.get(pk = 1)
	return render(request, 'tenant/index.html', locals())