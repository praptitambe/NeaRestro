from django.contrib import admin
from .models import Cuisine, Restaurant, Ratings, Comments


# Register your models here.
admin.site.register(Cuisine)
admin.site.register(Restaurant)
admin.site.register(Ratings)
admin.site.register(Comments)

