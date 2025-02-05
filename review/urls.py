from . import views
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.home, name='home'),
    path('restaurant/<slug:slug>/', views.restro_detail, name='restro_detail'),
]