from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from public.models import User, House

# Create your views here.
def index(request):
	print(request.session['account']['email'])
	#landlord = Landlord.objects.get(pk = 1)
	return render(request, 'landlord/index.html')

##### Landlord add house #####
def add_house(request):
	return render(request, 'landlord/add_house.html')

def manage_house(request):
	return render(request, 'landlord/manage_house.html')

def add_house_pic(request):
	return render(request, 'landlord/add_house_pic.html')