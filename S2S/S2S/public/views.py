from django.shortcuts import render

##### login page #####
def login(request):
	return render(request, 'public/login.html')

##### login page raw #####
def index(request):
	hello = 'hello, everyone'
	return render(request, 'public/index.html', {'hello': hello})

<<<<<<< HEAD

def search(request):
	return render(request, 'public/search.html')
=======
##### signup page #####
def signup(request):
	return render(request, 'public/signup.html')
>>>>>>> 6994ddb475429037f9de9b154874a42100c528a4

##### signup page raw #####
def Register(request):
	return render(request, 'public/Register.html')

<<<<<<< HEAD
def view_detail(request):
	return render(request, 'public/View_Detail.html')


=======

##### search house page #####
def Home(request):
	return render(request, 'public/Home.html')
>>>>>>> 6994ddb475429037f9de9b154874a42100c528a4

##### row houses page #####
def Display(request):
	return render(request, 'public/Display.html')

##### house detial page #####
def View_Detail(request):
	return render(request, 'public/View_Detail.html')





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
