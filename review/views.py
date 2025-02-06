from django.shortcuts import render, get_object_or_404
from .models import Restaurant,Ratings, Comments
from django.db.models import Avg

# Create your views here.
def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'review/home.html', {'restaurants': restaurants})

def restro_detail(request, slug):
    restaurant = get_object_or_404(Restaurant, slug=slug)
    average_rating = Ratings.objects.filter(restro=restaurant).aggregate(Avg('rating'))['rating__avg']
    comments = Comments.objects.filter(restro=restaurant)
    ratings = Ratings.objects.filter(restro=restaurant)
    comments = Comments.objects.all().order_by("-created_at")
    comment_count = Comments.objects.filter(is_approved=True).count()

    return render(request, 'review/restro_detail.html', {
        'restaurant': restaurant, 
        'average_rating': average_rating, 
        'comments': comments, 
        'ratings': ratings,
        "comments": comments,
        "comment_count": comment_count,
        })