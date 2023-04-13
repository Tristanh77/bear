from django.forms import ModelForm
from .models import Feeding 
from .models import BearFeeding 

class FeedingForm(ModelForm):
	class Meta:
		model = BearFeeding 
		fields = ['date', 'meal']