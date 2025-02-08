from django.urls import path
from . import views

 
urlpatterns = [
       path('', views.home, name='home'),
    path('restaurant/<slug:slug>/', views.restro_detail, name='restro_detail'),
    path('restaurant/<slug:slug>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('restaurant/<slug:slug>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]