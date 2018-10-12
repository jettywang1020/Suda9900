from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from public.models import User, House, Lease_Period, House_Rate, House_Comment
from public.help import *
from public.forms import *

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

def house_list(request):
	return render(request, 'tenant/house_list.html')

def post(request):
	return render(request,'tenant/post.html')

def house_detail(requet):
	return render(requet,'tenant/house_detail.html');

def history(request):
	id = request.session['account']['id'] if 'account' in request.session else 0
	sql = """SELECT * FROM lease_period WHERE period_end < CURDATE();"""
	lease_period = RunSQL(sql)
	list_info = []
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

	return render(request,'tenant/history.html', {'lp_list':list_info})

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

def edit_comm(request):
	return render(request,'tenant/edit_comm.html')