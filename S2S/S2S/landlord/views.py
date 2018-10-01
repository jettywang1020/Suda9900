from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from public.models import User, House, House_Picture
from public.forms import *
from public.help import *

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
			return render(request, 'public/index.html')
	return render(request, 'landlord/add_house.html',{'form': originalform})

def manage_house(request):
	id = request.session['account']['id'] if 'account' in request.session else 0
	sql = """select * from house"""
	houses_ = RunSQL(sql)
	houses = []
	for h in houses_:
		if h["user_id"] == id:
			try:
				picture = House_Picture.objects.get(house_id = h["id"])
				h["picture"] = picture
			except:
				continue
			houses.append(h)

	return render(request, 'landlord/manage_house.html', {'houses': houses})

def add_house_pic(request, id):
	originalform = addimage_form()
	house_pic = House_Picture.objects.all()
	pic_list = []
	for house_p in house_pic:
		if house_p.house_id == id:
			pic_list.append(house_p)

	if request.method == 'POST':
		form = addimage_form(request.POST,request.FILES)
		if form.is_valid():
			images = request.FILES.getlist("image")
			for image in images:
				house_pic = House_Picture(house_id = id, photo = image)
				house_pic.save()

			return render(request, 'landlord/add_house_pic.html', {'form': originalform, 'pic_list': pic_list})

	return render(request, 'landlord/add_house_pic.html', {'form': originalform, 'pic_list': pic_list})


def edit_house(request, id):
	house = House.objects.get(pk=id)
	originalform = addhouse_form()
	if request.method == 'POST':
		form = addhouse_form(request.POST)
		if form.is_valid():
			house.name = form.cleaned_data.get("name")
			house.address = form.cleaned_data.get("address")
			house.postcode = form.cleaned_data.get("postcode")
			house.hoprice = form.cleaned_data.get("price")
			house.profile = form.cleaned_data.get("profile")
			house.max_guest = form.cleaned_data.get("maxguest")
			house.no_of_beds = form.cleaned_data.get("bed")
			house.no_of_bedrooms = form.cleaned_data.get("bedroom")
			house.no_of_baths = form.cleaned_data.get("bathroom")
			house.no_of_parking = form.cleaned_data.get("park")
			house.tv = form.cleaned_data.get("tv")
			house.kitchen = form.cleaned_data.get("kitchen")
			house.washer = form.cleaned_data.get("washer")
			house.fridge = form.cleaned_data.get("fridge")
			house.conditioner = form.cleaned_data.get("conditioner")
			house.wifi = form.cleaned_data.get("wifi")
			house.studyroom = form.cleaned_data.get("studyroom")
			house.pool = form.cleaned_data.get("pool")
			house.house_rule = form.cleaned_data.get("rule")
			house.cancellation = form.cleaned_data.get("cancellation")
			house.extra = form.cleaned_data.get("extra")
			house.save(update_fields = ["name", "address", "postcode", "price", "profile"
						  , "max_guests", "no_of_beds", "no_of_bedrooms", "no_of_baths"
						  , "no_of_parking", "tv", "kitchen", "washer", "fridge"
						  , "conditioner", "wifi", "study_room", "pool", "house_rule"
						  , "cancellation", "extra"])
			return render(request, 'landlord/edit_house.html')
	return render(request, 'landlord/edit_house.html',{'form': originalform})

def history(request):
	return render(request, 'landlord/history.html')

def add_comm(request):
	return render(request, 'landlord/add_comm.html')
