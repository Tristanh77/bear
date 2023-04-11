from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Add the following import
from django.http import HttpResponse

from .models import Bear


class BearCreate(CreateView):
	model = Bear
	fields = '__all__' 
	success_url = '/index/'

class BearUpdate(UpdateView):
	model = Bear
	fields = '__all__'
	success_url = '/index/'

class BearDelete(DeleteView):
	model = Bear
	success_url = '/index/'

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