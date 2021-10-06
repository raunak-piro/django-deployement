from django.shortcuts import render
def index(request):
	return render(request,'myapp/index.html')
def other(request):
	return render(request,'myapp/other.html')

# Create your views here.
