from django.db import models
from django.urls import reverse



class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})

class Bear(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)

    def get_absolute_url(self):
		# return reverse('bears_detail', kwargs={'bear_id': self.id})
		# return reverse('bears_detail', kwargs={'bear_id': self.object.id})
        return reverse('bears_details', kwargs={'bear_id': self.id})
	

MEALS = (
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner'),
)
class BearFeeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
    bear = models.ForeignKey(Bear, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    class Meta:
        ordering = ['-date']

class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
    # bear = models.ForeignKey(Bear, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        # get_meal_display is automatically generated,
        # on inputs that have choices parameter, see meal
        return f"{self.get_meal_display()} on {self.date}"

