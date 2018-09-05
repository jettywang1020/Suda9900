from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from public.models import User, House
from public.forms import *

# Create your views here.
def index(request):
	print(request.session['account']['email'])
	#landlord = Landlord.objects.get(pk = 1)
	return render(request, 'landlord/index.html')

##### Landlord add house #####
def add_house(request):
	id = 1
	originalform = addhouse_form()
	if request.method == 'POST':
		form = addhouse_form(request.POST)
		if form.is_valid():
			name = form.cleaned_data.get("name")
			address = form.cleaned_data.get("address")
			postcode = form.cleaned_data.get("postcode")
			price = form.cleaned_data.get("price")
			profile = form.cleaned_data.get("profile")
			maxguest = form.cleaned_data.get("maxguest")
			bed = form.cleaned_data.get("bed")
			bedroom = form.cleaned_data.get("bedroom")
			bathroom = form.cleaned_data.get("bathroom")
			park = form.cleaned_data.get("park")
			tv = form.cleaned_data.get("tv")
			kitchen = form.cleaned_data.get("kitchen")
			washer = form.cleaned_data.get("washer")
			fridge = form.cleaned_data.get("fridge")
			conditioner = form.cleaned_data.get("conditioner")
			wifi = form.cleaned_data.get("wifi")
			studyroom = form.cleaned_data.get("studyroom")
			pool = form.cleaned_data.get("pool")
			rule = form.cleaned_data.get("rule")
			cancellation = form.cleaned_data.get("cancellation")
			extra = form.cleaned_data.get("extra")
			house = House(user_id = id, name = name, address = address, postcode = postcode, price = price, profile = profile
						  , max_guests = maxguest, no_of_beds = bed, no_of_bedrooms = bedroom, no_of_baths = bathroom
						  , no_of_parking = park, tv = tv, kitchen = kitchen, washer = washer, fridge = fridge
						  , conditioner = conditioner, wifi = wifi, study_room = studyroom, pool = pool, house_rule = rule
						  , cancellation = cancellation, extra = extra)
			house.save()
			request.session['house_account'] = {'id':house.id, 'user_id':id, 'name':name,'address':address, 'postcode':postcode, 'price':price
												, 'profile':profile, 'max_guests':maxguest, 'no_of_beds':bed, 'no_of_bedrooms':bedroom
												, 'no_of_baths':bathroom, 'no_of_parking':park, 'tv':tv, 'kitchen':kitchen, 'washer':washer
												, 'fridge':fridge, 'conditioner':conditioner, 'wifi':wifi, 'study_room':studyroom, 'pool':pool
												, 'house_rule':rule, 'cancellation':cancellation, 'extra':extra}
	return render(request, 'landlord/add_house.html',{'form': originalform})

def manage_house(request):
	return render(request, 'landlord/manage_house.html')

def add_house_pic(request):
	return render(request, 'landlord/add_house_pic.html')