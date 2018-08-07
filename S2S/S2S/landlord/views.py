from django.shortcuts import render
from public.models import Tenant, Landlord, House

# Create your views here.
def index(request):
	landlord = Landlord.objects.get(pk = 1)
	return render(request, 'landlord/index.html', {'landlord': landlord})