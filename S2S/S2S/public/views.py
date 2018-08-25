from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from public.models import Tenant, Landlord, House

from public.forms import login_form, signup_form

##### login page #####
def login(request):
	originalform = login_form()
	if request.method == 'POST':
		form = login_form(request.POST)
		if form.is_valid():
			email = form.cleaned_data.get("email")
			password = form.cleaned_data.get("password")
			is_landlord = form.cleaned_data.get("is_landlord")
		return render(request, 'public/login.html', {'form': originalform})
	else:
		return render(request, 'public/login.html', {'form': originalform})


##### login page raw #####
def index(request):
	hello = 'hello, everyone'
	return render(request, 'public/index.html', {'hello': hello})

##### signup page #####
def signup(request):
	originalform = signup_form()
	if request.method == 'POST':
		form = signup_form(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			first_name = form.cleaned_data.get("first_name")
			last_name = form.cleaned_data.get("last_name")
			email = form.cleaned_data.get("email")
			password = form.cleaned_data.get("password")
			confirm_password = form.cleaned_data.get("confirm_password")
			is_landlord = form.cleaned_data.get("is_landlord")
		return render(request, 'public/signup.html', {'form': originalform})
	else:
		return render(request, 'public/signup.html', {'form': originalform})

##### signup page raw #####
def register(request):
	return render(request, 'public/register.html')


##### search house page #####
def home(request):
	return render(request, 'public/home.html')

##### row houses page #####
def display(request):
	return render(request, 'public/display.html')

##### house detial page #####
def view_detail(request):
	return render(request, 'public/view_detail.html')





def RunSQL(sql):
	with connection.cursor() as cursor:
		cursor.execute(sql)
		rows = cursor.fetchall()
		fieldnames = [name[0] for name in cursor.description]
		results = []
		for row in rows:
			result = {}
			for i in range(len(row)):
				result[fieldnames[i]] = row[i]
			results.append(result)
	return results
