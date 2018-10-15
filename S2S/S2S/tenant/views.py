from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from public.models import User, House, Lease_Period, House_Rate, House_Comment, Post
from public.help import *
from public.forms import *

def help(request):
	return render(request, 'tenant/help.html')

def post_list(request):
	sql = """select * from post"""
	posts = RunSQL(sql)
	return render(request, 'tenant/post_list.html',{'posts': posts})

def post(request):
	user_id = request.session['account']['id'] if 'account' in request.session else 0
	originalform = post_form()
	if request.method == 'POST':
		form = post_form(request.POST)
		if form.is_valid():
			title = form.cleaned_data.get("title")
			area = form.cleaned_data.get("area")
			no_of_rooms = form.cleaned_data.get("no_of_rooms")
			rent_type = form.cleaned_data.get("rent_type")
			description = form.cleaned_data.get("description")
			name = form.cleaned_data.get("name")
			email = form.cleaned_data.get("email")
			mobile = form.cleaned_data.get("mobile")
			post = Post(user_id = user_id, title = title, area = area, no_of_rooms = no_of_rooms, rent_type = rent_type, description = description, name = name, email = email, mobile = mobile)
			post.save()
			return redirect('tenant:post_list')
		else:
			return render(request,'tenant/post.html', {'form':originalform})
	return render(request,'tenant/post.html', {'form':originalform})

def post_detail(request, id):
	try:
		post = Post.objects.get(pk=id)
		return render(request,'tenant/post_detail.html', {'post':post})
	except:
		return redirect('tenant:post_list')

def history(request):
	id = request.session['account']['id'] if 'account' in request.session else 0
	sql = """SELECT * FROM lease_period WHERE period_end < CURDATE();"""
	lease_period = RunSQL(sql)
	list_info = []
	list_info_future = []
	for lp in lease_period:
		if lp['user_id'] == id:
			house = House.objects.get(pk=lp['house_id'])
			house_info = {}
			house_info["id"] = lp['house_id']
			house_info["name"] = house.name
			house_info["address"] = house.address
			house_info["period_start"] = lp['period_start']
			house_info["period_end"] = lp['period_end']
			picture = House_Picture.objects.all()
			for pic in picture:
				if pic.house_id == lp['house_id']:
					house_info["picture"] = pic
					break
			list_info.append(house_info)
	sql = """SELECT * FROM lease_period WHERE period_end >= CURDATE();"""
	lease_period = RunSQL(sql)
	for lp in lease_period:
		if lp['user_id'] == id:
			house = House.objects.get(pk=lp['house_id'])
			house_info = {}
			house_info["id"] = lp['house_id']
			house_info["name"] = house.name
			house_info["address"] = house.address
			house_info["period_start"] = lp['period_start']
			house_info["period_end"] = lp['period_end']
			picture = House_Picture.objects.all()
			for pic in picture:
				if pic.house_id == lp['house_id']:
					house_info["picture"] = pic
					break
			list_info_future.append(house_info)

	return render(request,'tenant/history.html', {'lp_list':list_info,'lp_list_future':list_info_future})

def add_comm(request, id):
	user_id = request.session['account']['id'] if 'account' in request.session else 0
	house_id = id
	originalform = hcomment_form()
	if request.method == 'POST':
		form = hcomment_form(request.POST)
		if form.is_valid():
			accuracy = form.cleaned_data.get("accuracy")
			communication = form.cleaned_data.get("communication")
			location = form.cleaned_data.get("location")
			checkin = form.cleaned_data.get("checkin")
			cleanliness = form.cleaned_data.get("cleanliness")
			value = form.cleaned_data.get("value")
			comment = form.cleaned_data.get("comment")
			house_rate = House_Rate.objects.all()
			for house_r in house_rate:
				if house_r.user_id == user_id and house_r.house_id == house_id:
					print('already added')
					break
			else:
				house_rate = House_Rate(user_id = user_id, house_id = house_id, accuracy = accuracy, communication = communication
										, location = location, check_in = checkin, cleanliness = cleanliness, value = value)
				house_rate.save()
				house_comment = House_Comment(user_id = user_id, house_id = house_id, comment = comment)
				house_comment.save()	

			sql = """SELECT * FROM lease_period WHERE period_end < CURDATE();"""
			lease_period = RunSQL(sql)
			list_info = []
			for lp in lease_period:
				house = House.objects.get(pk=lp['house_id'])
				house_info = {}
				house_info["id"] = lp['house_id']
				house_info["name"] = house.name
				house_info["address"] = house.address
				house_info["period_start"] = lp['period_start']
				house_info["period_end"] = lp['period_end']
				try:
					picture = House_Picture.objects.get(house_id = lp['house_id'])
					house_info["picture"] = picture	
				except:
					continue
				list_info.append(house_info)

			return render(request, 'tenant/history.html', {'lp_list':list_info})	
	return render(request,'tenant/add_comm.html', {'form':originalform})

# apply to be the landlord
def apply_page(request):
	return render(request,'tenant/apply.html')

def apply(request):
	id = request.session['account']['id'] if 'account' in request.session else 0
	user = User.objects.get(pk=id)
	user.is_landlord = True
	user.save(update_fields = ["is_landlord"])
	request.session['account'] = {'id':user.id, 'username':user.username, 'email':user.email, 'activate':user.activate, 'is_landlord':user.is_landlord}
	return redirect('public:profile')
