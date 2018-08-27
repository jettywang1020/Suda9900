from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password, check_password

from public.models import *
from public.forms import *
from public.help import *

##### login page #####
def login(request):
	originalform = login_form()
	# if request.method == 'POST':
	# 	form = login_form(request.POST)
	# 	if form.is_valid():
	# 		email = form.cleaned_data.get("email")
	# 		password = form.cleaned_data.get("password")
	# 		is_landlord = form.cleaned_data.get("is_landlord")
	# 		if is_landlord :
	# 			user = Landlord.objects.filter(email=email)
	# 		else:
	# 			user = Tenant.objects.filter(email=email)

	# 		if len(user) == 1 :
	# 			if check_password(password, user[0].password):
	# 				request.session['account'] = {'id':user[0].id, 'username':user[0].username, 'email':user[0].email, 'activate':user[0].activate}
	# 				return render(request, 'public/index.html')
	# 			else:
	# 				error = "Incorrect password!"
	# 				return render(request, 'public/login.html', {'form': originalform, 'error': error}) 

	# 		else:
	# 			error = "Account does not exist!"
	# 			return render(request, 'public/login.html', {'form': originalform, 'error': error})
	# else:
	return render(request, 'public/login.html', {'form': originalform})

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
		
			if password != confirm_password:
				error = "Passwords don't match!"
				return render(request, 'public/signup.html', {'form': originalform, 'error': error})
			elif len(password) < 6 :
				error = "Please make sure the length of your password is not shorter than 6!"
				return render(request, 'public/signup.html', {'form': originalform, 'error': error})
			else:
				user_email = User.objects.filter(email = email, is_landlord = is_landlord)
				user_username = User.objects.filter(username = username, is_landlord = is_landlord)
		

				
				if len(user_email) > 0 and len(user_username) == 0:
					error = "This email has been used!"
					return render(request, 'public/signup.html', {'form': originalform, 'error': error})
				elif len(user_email) == 0 and len(user_username) > 0:
					error = "This username has been used!"
					return render(request, 'public/signup.html', {'form': originalform, 'error': error})
				elif len(user_email) > 0 and len(user_username) > 0:
					error = "The username and email have been used!"
					return render(request, 'public/signup.html', {'form': originalform, 'error': error})
				else:
					password = make_password(password, None, 'pbkdf2_sha256')
					user = User(username = username, email = email, password = password, first_name = first_name, last_name = last_name, is_landlord = is_landlord)

					user.save()
					request.session['account'] = {'id':user.id, 'username':username, 'email':email, 'activate':False}

					return render(request, 'public/login.html')

	else:
		return render(request, 'public/signup.html', {'form': originalform})


##### login page raw #####
def index(request):
	hello = 'hello, everyone'
	return render(request, 'public/index.html', {'hello': hello})

def search(request):
	return render(request, 'public/search.html')


def view_detail(request):
	return render(request, 'public/ciew_detail.html')


def home(request):
	return render(request, 'public/home.html')


##### row houses page #####
def display(request):
	return render(request, 'public/display.html')

##### house detial page #####
def view_detail(request):
	return render(request, 'public/view_detail.html')
