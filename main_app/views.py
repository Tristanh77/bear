from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

from .models import Bear


# Define the home view
def home(request):
  return render(request, 'home.html')

def bear_index(request):
  bears = Bear.objects.all()
  return render(request, 'bears/index.html', {'bears': bears})

def about(request):
  return render(request, 'about.html')

def bears_detail(request, bear_id):
	bear = Bear.objects.get(id=bear_id) 
	return render(request, 'bears/detail.html', {'bear': bear})