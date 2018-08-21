from django.shortcuts import render

# Create your views here.
def index(request):
	hello = 'hello, everyone'
	return render(request, 'public/index.html', {'hello': hello})

def test(request):
	return render(request, 'public/Home.html')