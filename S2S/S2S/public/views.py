from django.shortcuts import render

# Create your views here.
def index(request):
	hello = 'hello, everyone'
	return render(request, 'public/index.html', {'hello': hello})

def Home(request):
	return render(request, 'public/Home.html')

def Register(request):
	return render(request, 'public/Register.html')

def View_Detail(request):
	return render(request, 'public/View_Detail.html')