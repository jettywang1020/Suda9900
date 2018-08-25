from django.shortcuts import render


def login(request):
	return render(request, 'public/login.html')

def signup(request):
	return render(request, 'public/signup.html')


# Create your views here.
def index(request):
	hello = 'hello, everyone'
	return render(request, 'public/index.html', {'hello': hello})


def search(request):
	return render(request, 'public/search.html')

def Register(request):
	return render(request, 'public/Register.html')

def view_detail(request):
	return render(request, 'public/View_Detail.html')



# display home page with eight images
def Display(request):
	return render(request, 'public/Display.html')



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
