from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Add the following import
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Bear


class BearCreate(CreateView):
	model = Bear
	fields = '__all__' 
	template_name = 'main_app/bear_form.html'

	def get_success_url(self):	
		bear_id = self.object.id
		bear = Bear.objects.get(id=bear_id)
		bear_id = bear.id	
		return reverse_lazy("bear_details", kwargs={"bear_id": bear_id})


class BearUpdate(UpdateView):
	model = Bear
	fields = '__all__'

	

class BearDelete(DeleteView):
	model = Bear
	success_url = '/bears/'

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

