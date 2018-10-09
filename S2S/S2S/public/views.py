from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password, check_password

import datetime
import re

from public.models import *
from public.forms import *
from public.help import *
from public.KNN import knn_model

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
					request.session['account'] = {'id':user[0].id, 'username':user[0].username, 'email':user[0].email, 'activate':user[0].activate, 'is_landlord':user[0].is_landlord}
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
		request.session['account'] = None
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

def other_profile(request):
	return render(request,'public/other_profile.html')

def search(request):
	if request.method == 'POST':
		keyword = request.POST.get("keyword", "keyword")
		sql = """select * from house
		 WHERE lower(name) like lower('%""" + keyword + """%') 
		 or lower(address) like lower('%""" + keyword + """%') 
		 or lower(profile) like lower('%""" + keyword + """%')"""
		houses = RunSQL(sql)
		for house in houses:
			picture = House_Picture.objects.all()
			for pic in picture:
				if pic.house_id == house["id"]:
					house["picture"] = pic
					break
		return render(request, 'public/display.html', locals())

def adv_search(request):
	originalform = adv_search_form()
	if request.method == 'POST':
		form = adv_search_form(request.POST)
		if form.is_valid():
			keyword = form.cleaned_data.get("keyword")
			check_in = form.cleaned_data.get("check_in")
			check_out = form.cleaned_data.get("check_out")
			adult = form.cleaned_data.get("adult")
			children = form.cleaned_data.get("children")
			
			check_in = check_in.split("/")
			check_out = check_out.split("/")
			check_in = int(check_in[2])*10000 + int(check_in[1])*100 + int(check_in[0])*1
			check_out = int(check_out[2])*10000 + int(check_out[1])*100 + int(check_out[0])*1
			current_date = datetime.datetime.now().year*10000 +  datetime.datetime.now().month*100 +  datetime.datetime.now().day

			if check_in < current_date:
				print(current_date)
				error = "Invalid Date Period!"
				return render(request, 'public/adv_search.html',{"form":originalform, "error":error})
			elif check_out <= check_in:
				error = "Invalid Date Period!"
				return render(request, 'public/adv_search.html',{"form":originalform, "error":error})
			else:
				total_guests = int(adult) + int(children)
				sql = """select * from house
				 WHERE (lower(name) like lower('%""" + keyword + """%') 
				 or lower(address) like lower('%""" + keyword + """%') 
				 or lower(profile) like lower('%""" + keyword + """%'))
				 and max_guests >= """ + str(total_guests) + """;"""
				houses = RunSQL(sql)
				# 日期校验在这里
				for house in houses:
					picture = House_Picture.objects.all()
					for pic in picture:
						if pic.house_id == house["id"]:
							house["picture"] = pic
							break
				return render(request, 'public/display.html', locals())
		return render(request, 'public/adv_search.html',{"form":originalform})
	else:
		return render(request, 'public/adv_search.html',{"form":originalform})

def view_detail(request, id):
	house_feature_r = [0 for _ in range(12)]
	reviews = 0
	pic_1 = None
	pic_list = []
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
	house_comment = House_Comment.objects.all()
	house_comment_ = []
	for temp in house_comment:
		if temp.house_id == id:
			comment = temp.comment
			comment_date = temp.time_stamp
			user_id = temp.user_id
			user = User.objects.all()
			for u in user:
				if u.id == user_id:
					photo = u.photo
					c_name = u.username
			house_comment_.append({'user_id':user_id, 'comment':comment, 'comment_date':comment_date, 'photo':photo, 'comment_user':c_name})

	house_pic = House_Picture.objects.all()	
	num = 1		
	for house_p in house_pic:
		if num == 1 and house_p.house_id == id:
			pic_1 = house_p
			num += 1
		elif house_p.house_id == id:
			pic_list.append(house_p)
			num += 1
	context = {'house_id':house.id,'house_name':house.name,'house_postcode':house.postcode,'house_address':house.address,'guests_num':house.max_guests
				,'bedrooms_num':house.no_of_bedrooms,'beds_num':house.no_of_beds,'baths_num':house.no_of_baths,'house_parking':house.no_of_parking
				,'house_profile':house.profile,'house_price':house.price,'house_rule':house.house_rule,'house_cancellation':house.cancellation
				,'house_extra':house.extra,'house_tv':house.tv,'house_kitchen':house.kitchen,'house_washer':house.washer
				,'house_fridge':house.fridge,'house_conditioner':house.conditioner,'house_wifi':house.wifi,'house_studyroom':house.study_room
				,'house_pool':house.pool,'house_accuracy':house_feature['accuracy'],'house_location':house_feature['location']
				,'house_communication':house_feature['communication'],'house_checkin':house_feature['check_in'],'house_cleanliness':house_feature['cleanliness']
				,'house_value':house_feature['value'],'house_reviews':reviews, 'house_comment':house_comment_, 'house_pic':pic_list, 'pic_1':pic_1}
	return render(request, 'public/view_detail.html', context)


def display(request):
	sql = """select * from house"""
	houses = RunSQL(sql)
	relate = []
	try:
		id = request.session['account']['id'] if 'account' in request.session else 0

	except:
		for house in houses:
			picture = House_Picture.objects.all()
			for pic in picture:
				if pic.house_id == house["id"]:
					house["picture"] = pic
					break
		return render(request, 'public/display.html', {'houses':houses,'r_houses':relate})
	result_ = 0
	house_tag_list = {}
	# sql = """SELECT * FROM lease_period WHERE period_end < CURDATE();"""
	sql = """SELECT * FROM lease_period """
	lease_period = RunSQL(sql)
	list_info = [0 for _ in range(len(Tag.objects.all()))]
	for lp in lease_period:
		if lp['user_id'] == id:
			house_tag = House_Tag.objects.all()
			for h in house_tag:
				if h.house_id == lp['house_id']:
					list_info[h.tag_id - 1] += 1
	if sum(list_info) == 0:
		for house in houses:
			picture = House_Picture.objects.all()
			for pic in picture:
				if pic.house_id == house["id"]:
					house["picture"] = pic
					break
		return render(request, 'public/display.html', {'houses':houses,'r_houses':relate})
	else:
		for i in range(len(list_info)):
			list_info[i] = list_info[i]/sum(list_info)

		result = knn_model([list_info])
		sql = """select * from house_tag"""
		house_relate = RunSQL(sql)
		for i in house_relate:
			house_tag_list[i['house_id']] = 0
		for i in house_relate:
			house_tag_list[i['house_id']] = house_tag_list[i['house_id']]*10 + i['tag_id']

		for i in range(len(result)):
			if result[i] == 1:
				result_ = result_*10+(i+1)
		for house in houses:
			try:
				if house_tag_list[house['id']] == result_:

					relate.append(house)
			except:
				continue

		for house in houses:
			picture = House_Picture.objects.all()
			for pic in picture:
				if pic.house_id == house["id"]:
					house["picture"] = pic
					break
		return render(request, 'public/display.html', {'houses':houses,'r_houses':relate})

def profile(request):
	id = request.session['account']['id'] if 'account' in request.session else 0
	user = User.objects.get(pk=id)
	originalform = profile_form()
	if request.method == 'POST':
		form = profile_form(request.POST)
		if form.is_valid():
			user.username = form.cleaned_data.get("username")
			user.first_name = form.cleaned_data.get("firstname")
			user.last_name = form.cleaned_data.get("lastname")
			user.email = form.cleaned_data.get("email")
			user.gender = form.cleaned_data.get("gender")
			user.dob = form.cleaned_data.get("dob")
			dob = re.search(r'^(\d{2}/)?(\d{2}/)?(\d{4})$',user.dob)
			new_dob = dob.group(3) + '-' + dob.group(2)[:-1] + '-' + dob.group(1)[:-1]
			user.dob = new_dob
			user.phone = form.cleaned_data.get("phone")
			user.profile = form.cleaned_data.get("profile")
			user.save(update_fields = ["username","first_name","last_name","email","gender","dob","phone","profile"])
			request.session['account'] = {'id':user.id, 'username':user.username, 'email':user.email, 'activate':user.activate, 'is_landlord':user.is_landlord}
			return redirect('public:profile')
	else:
		originalform = profile_form(initial = {'username': user.username, 'firstname': user.first_name, 'lastname': user.last_name, 'gender':user.gender, 'dob':user.dob, 'phone':user.phone, 'email':user.email, 'profile':user.profile})						   
		return render(request, 'public/profile.html', {'form': originalform})

def upload_photo(request):
	id = request.session['account']['id'] if 'account' in request.session else 0
	user = User.objects.get(pk=id)
	originalform = upload_photo_form()
	if request.method == 'POST':
		form = upload_photo_form(request.POST, request.FILES)
		if form.is_valid():
			photo = request.FILES.getlist("photo")[0]
			user = User(pk=id, photo=photo)
			user.save()
			return redirect('public:upload_photo')
	return render(request, 'public/upload_photo.html', {'form':originalform, 'photo':user.photo})


def book(request):
	user_id = request.session['account']['id'] if 'account' in request.session else 0
	if request.method == 'POST':
		house_id = request.POST.get("house_id",None)
		check_in = request.POST.get("check_in",None)
		check_out = request.POST.get("check_out",None)
		adult = request.POST.get("adult",None)
		children = request.POST.get("children",None)

		if house_id and check_in and check_out and adult and children:
			print(house_id, check_in, check_out, adult, children)
			house_id = int(house_id)
			check_in = check_in.split("/")
			check_out = check_out.split("/")
			new_check_in = check_in[2] + "-" + check_in[1] + "-" + check_in[0]
			new_check_out = check_out[2] + "-" + check_out[1] + "-" + check_out[0]
			check_in = int(check_in[2])*10000 + int(check_in[1])*100 + int(check_in[0])*1
			check_out = int(check_out[2])*10000 + int(check_out[1])*100 + int(check_out[0])*1
			current_date = datetime.datetime.now().year*10000 +  datetime.datetime.now().month*100 +  datetime.datetime.now().day
			adult =  int(adult)
			children =  int(children)


			# date check
			if check_in < current_date:
				print(current_date)
				message = "Invalid Date Period!"
				return render(request, 'public/blank.html', {'message':message})
			elif check_out <= check_in:
				message = "Invalid Date Period!"
				return render(request, 'public/blank.html', {'message':message})

			# guest amount check
			sql = """ select * from house where id = """ + str(house_id) + """;""";
			house = RunSQL(sql)[0]
			if house['max_guests'] < adult + children:
				message = "Too many guests!"
				return render(request, 'public/blank.html', {'message':message})

			# date check again
			sql = """ select * from lease_period where house_id = """ + str(house_id) + """ and period_end > CURDATE();""";
			records = RunSQL(sql)
			available = 1;
			for record in records:
				start = record['period_start'].split("-")
				new_start = int(start[2])*10000 + int(start[1])*100 + int(start[0])*1
				end = record['period_end'].split("-")
				new_end = int(end[2])*10000 + int(end[1])*100 + int(end[0])*1

				if start > check_out or end < check_in:
					continue
				else:
					available = 0
			if(available == 0):
				message = "House is not available during this period!"
				return render(request, 'public/blank.html', {'message':message})
			else:
				book = Lease_Period(house_id = house_id, user_id = user_id, period_start = new_check_in, period_end = new_check_out)
				book.save()
				message = "Success!"
				return render(request, 'public/blank.html', {'message':message})
			
		else:
			message = "Bad Request!"
			return render(request, 'public/blank.html', {'message':message})
	else:
		message = "Bad Request!"
		return render(request, 'public/blank.html', {'message':message})




def other_profile(request, id):
	user = User.objects.get(pk=id)
	user_rate = User_Rate.objects.all()
	user_r = 0
	num = 0
	for ur in user_rate:
		if ur.user2_id == id:
			user_r += ur.reputation
			num += 1
	user_r = round(float(user_r)/num)
	return render(request, 'public/other_profile.html', {'user':user, 'user_rate':user_r})

