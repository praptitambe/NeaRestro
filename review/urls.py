from . import views
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.home, name='home'),
    path('restaurant/<slug:slug>/', views.restro_detail, name='restro_detail'),
    path('restaurant/<slug:slug>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
]