from django.shortcuts import render


def login(request):
	return render(request, 'public/login.html')

def signup(request):
	return render(request, 'public/signup.html')


# Create your views here.
def index(request):
	hello = 'hello, everyone'
	return render(request, 'public/index.html', {'hello': hello})

<<<<<<< HEAD
def Home(request):
	return render(request, 'public/Home.html')

def Register(request):
	return render(request, 'public/Register.html')

def View_Detail(request):
	return render(request, 'public/View_Detail.html')
=======
def test(request):
	return render(request, 'public/Home.html')

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
>>>>>>> 6f6fe038488bc8defdd0fb640013d263b231ad19
