from django.contrib import admin
from .models import Cuisine, Restaurant, Comments


# Register your models here.
admin.site.register(Cuisine)
admin.site.register(Restaurant)
admin.site.register(Comments)
