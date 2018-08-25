from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from public.models import Tenant, Landlord, House

# Create your views here.
def index(request):
	landlord = Landlord.objects.get(pk = 1)
	return render(request, 'landlord/index.html', {'landlord': landlord})


def login(request):
	originalform = login_form()
	if request.method == 'POST':
		form = login_form(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			print(username, password)
		return render(request, 'landlord/login.html', {'form': originalform})
	else:
		return render(request, 'landlord/login.html', {'form': originalform})


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