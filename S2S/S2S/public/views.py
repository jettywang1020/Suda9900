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
		return render(request, 'public/search.html', {'form': originalform})

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

def view_detail(request):
	return render(request, 'public/view_detail.html')

def display(request):
	sql = """select * from house"""
	houses = RunSQL(sql)

	for house in houses:
		picture = House_Picture.objects.get(house_id = house["id"])
		house["picture"] = picture

	return render(request, 'public/display.html', locals())

def profile(request):
	return render(request, 'public/profile.html')
