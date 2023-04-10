from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Bear:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

bears = [
  Bear('Beary Barrington', 'grizzley', 'fan of The Country Bears', 0),
  Bear('Big Al', 'gray', 'overweight', 10),
  Bear('Ted Bedderhead', 'brown', 'lead singer', 4)
]
# Define the home view
def home(request):
  return render(request, 'home.html')

def bear_index(request):
  return render(request, 'bears/index.html', {'bears': bears})

def about(request):
  return render(request, 'about.html')