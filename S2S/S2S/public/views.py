from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password, check_password

from public.models import *
from public.forms import *
from public.help import *

##### login page #####
def login(request):
	originalform = login_form()
	if request.method == 'POST':
		form = login_form(request.POST)
		if form.is_valid():
			email = form.cleaned_data.get("email")
			password = form.cleaned_data.get("password")
			user = User.objects.filter(email = email)

			if len(user) == 1 :
				if check_password(password, user[0].password):
					request.session['account'] = {'id':user[0].id, 'username':user[0].username, 'email':user[0].email, 'activate':user[0].activate}
					return render(request, 'public/index.html')
				else:
					error = "Incorrect password!"
					return render(request, 'public/login.html', {'form': originalform, 'error': error}) 
			else:
				error = "Account does not exist!"
				return render(request, 'public/login.html', {'form': originalform, 'error': error})
	else:
		return render(request, 'public/login.html', {'form': originalform})

##### logout #####
def logout(request):
	try:
		del request.session['account']
	except:
		pass
	return redirect('public:login')


##### signup page #####
def signup(request):
	originalform = signup_form()
	if request.method == 'POST':
		form = signup_form(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			email = form.cleaned_data.get("email")
			password = form.cleaned_data.get("password")
			confirm_password = form.cleaned_data.get("confirm_password")
			gender = form.cleaned_data.get("gender")
		
			if password != confirm_password:
				error = "Passwords don't match!"
				return render(request, 'public/signup.html', {'form': originalform, 'error': error})
			elif len(password) < 6 :
				error = "Please make sure the length of your password is not shorter than 6!"
				return render(request, 'public/signup.html', {'form': originalform, 'error': error})
			else:
				user = User.objects.filter(email = email)
		
				if len(user) > 0:
					error = "This email has been used!"
					return render(request, 'public/signup.html', {'form': originalform, 'error': error})
				else:
					password = make_password(password, None, 'pbkdf2_sha256')
					user = User(username = username, email = email, password = password, gender = gender)

					user.save()
					request.session['account'] = {'id':user.id, 'username':username, 'email':email, 'activate':False, 'is_landlord':False}

					return render(request, 'public/login.html')

	else:
		return render(request, 'public/signup.html', {'form': originalform})


def index(request):
	hello = 'hello, everyone'
	return render(request, 'public/index.html', {'hello': hello})

def search(request):
	return render(request, 'public/search.html')

def view_detail(request,id):
	id  =  id
	house_feature_r = [0 for _ in range(12)]
	reviews = 0
	house_feature = {'accuracy':0,'location':0,'communication':0,'check_in':0,'cleanliness':0,'value':0}
	house = House.objects.get(pk=id)
	house_rate = House_Rate.objects.all()
	if house_rate:
		for house_r in house_rate:
			if house_r.house_id == id:
				house_feature_r[0] += house_r.accuracy
				house_feature_r[1] += 1
				house_feature_r[2] += house_r.location
				house_feature_r[3] += 1
				house_feature_r[4] += house_r.communication
				house_feature_r[5] += 1
				house_feature_r[6] += house_r.check_in
				house_feature_r[7] += 1
				house_feature_r[8] += house_r.cleanliness
				house_feature_r[9] += 1
				house_feature_r[10] += house_r.value
				house_feature_r[11] += 1
		if house_feature_r[1]:
			house_feature['accuracy'] = round(house_feature_r[0]/house_feature_r[1])
			reviews += house_feature['accuracy']
		if house_feature_r[3]:
			house_feature['location'] = round(house_feature_r[2]/house_feature_r[3])
			reviews += house_feature['location']
		if house_feature_r[5]:
			house_feature['communication'] = round(house_feature_r[4]/house_feature_r[5])
			reviews += house_feature['communication']
		if house_feature_r[7]:
			house_feature['check_in'] = round(house_feature_r[6]/house_feature_r[7])
			reviews += house_feature['check_in']
		if house_feature_r[9]:
			house_feature['cleanliness'] = round(house_feature_r[8]/house_feature_r[9])
			reviews += house_feature['cleanliness']
		if house_feature_r[11]:
			house_feature['value'] = round(house_feature_r[10]/house_feature_r[11])
			reviews += house_feature['value']
		reviews = round(reviews/6)
	
	context = {'house_name':house.name,'house_postcode':house.postcode,'house_address':house.address,'guests_num':house.max_guests
				,'bedrooms_num':house.no_of_bedrooms,'beds_num':house.no_of_beds,'baths_num':house.no_of_baths,'house_parking':house.no_of_parking
				,'house_profile':house.profile,'house_price':house.price,'house_rule':house.house_rule,'house_cancellation':house.cancellation
				,'house_extra':house.extra,'house_tv':house.tv,'house_kitchen':house.kitchen,'house_washer':house.washer
				,'house_fridge':house.fridge,'house_conditioner':house.conditioner,'house_wifi':house.wifi,'house_studyroom':house.study_room
				,'house_pool':house.pool,'house_accuracy':house_feature['accuracy'],'house_location':house_feature['location']
				,'house_communication':house_feature['communication'],'house_checkin':house_feature['check_in'],'house_cleanliness':house_feature['cleanliness']
				,'house_value':house_feature['value'],'house_reviews':reviews}
	return render(request, 'public/view_detail.html', context)


def display(request):
	sql = """select * from house"""
	houses = RunSQL(sql)
	
	for house in houses:
		try:
			picture = House_Picture.objects.get(house_id = house["id"])
			house["picture"] = picture
		except:
			continue
	return render(request, 'public/display.html', locals())

def profile(request):
	# id = request.session['account'].id
	originalform = profile_form()
	if request.method == 'POST':
		form = profile_form(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			firstname = form.cleaned_data.get("firstname")
			lastname = form.cleaned_data.get("lastname")
			email = form.cleaned_data.get("email")
			gender = form.cleaned_data.get("gender")
			dob = form.cleaned_data.get("dob")
			phone = form.cleaned_data.get("phone")
			profile = form.cleaned_data.get("profile")
			user = User(username = username, first_name = firstname, last_name = lastname, email = email, gender = gender, dob = dob
						, phone = phone, profile = profile)
			user.save()
			request.session['account'] = {'id':user.id, 'username':username, 'firstname':firstname, 'lastname':lastname, 'email':email, 'dob':dob, 'gender':gender, 'phone':phone
										   , 'profile':profile}
			return render(request, 'public/index.html')							   
	return render(request, 'public/profile.html', {'form': originalform})
