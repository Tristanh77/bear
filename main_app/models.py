from django.db import models
from django.urls import reverse

class Bear(models.Model):
	name = models.CharField(max_length=100)
	breed = models.CharField(max_length=100)
	description = models.TextField(max_length=250)
	age = models.IntegerField()
# Create your models here.

	def get_absolute_url(self):
		# return reverse('bears_detail', kwargs={'bear_id': self.id})
		# return reverse('bears_detail', kwargs={'bear_id': self.object.id})
		return reverse('bears_details', kwargs={'bear_id': self.id})