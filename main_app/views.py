from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Add the following import
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Bear, Toy
from .forms import FeedingForm


def assoc_toy(request, bear_id, toy_id):
	Bear.objects.get(id=bear_id).toys.add(toy_id)

	return redirect('bears_detail', bear_id=bear_id)

class BearCreate(CreateView):
	model = Bear
	fields = ['name', 'breed', 'description', 'age'] 
	template_name = 'main_app/bear_form.html'

	def get_success_url(self):	
		bear_id = self.object.id
		bear = Bear.objects.get(id=bear_id)
		bear_id = bear.id	
		return reverse_lazy("bears_detail", kwargs={"bear_id": bear_id})



class BearUpdate(UpdateView):
	model = Bear
	fields = ['name', 'breed', 'description', 'age'] 

	def get_success_url(self):	
		bear_id = self.object.id
		bear = Bear.objects.get(id=bear_id)
		bear_id = bear.id	
		return reverse_lazy("bears_detail", kwargs={"bear_id": bear_id})
	

class BearDelete(DeleteView):
	model = Bear
	success_url = '/bears/'

def add_feeding(request, bear_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_bearfeeding = form.save(commit=False)
        new_bearfeeding.bear_id = bear_id
        new_bearfeeding.save()
    return redirect('bears_detail', bear_id=bear_id)



# Define the home view
def home(request):
  return render(request, 'home.html')

def bear_index(request):
  bears = Bear.objects.all()
  return render(request, 'bears/index.html', {'bears': bears})

def about(request):
  return render(request, 'about.html')

def bears_detail(request, bear_id):
    # find the cat with the id that was in the params in the db
    bear = Bear.objects.get(id=bear_id)
    # Find all the toys not in the cat.toys.all() array

    # cat.toys.all().values_list('id') <- this finds all the cats toys and returns a list
    # of just their id's
    #  Find all toys that are not in the cat.toys id list
	# id__in <- Field Look up, theser for complicated queries 
    toys_bear_doesnt_have = Toy.objects.exclude(
        id__in=bear.toys.all().values_list('id'))

    # creating a form (instance) from our FeedingForm class!
    feeding_form = FeedingForm()
    return render(request, 'bears/detail.html', {
		'bear': bear, 
		'feeding_form': feeding_form, 
		'toys': toys_bear_doesnt_have
	})


class ToyList(ListView):
    model = Toy


class ToyDetail(DetailView):
    model = Toy


class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'


class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']


class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

