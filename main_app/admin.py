from django.contrib import admin

# Register your models here.
from .models import Bear, BearFeeding, Toy

admin.site.register(Bear)
admin.site.register(BearFeeding)
admin.site.register(Toy)