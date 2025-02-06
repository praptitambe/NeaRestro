from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from django.contrib import messages
from .models import Restaurant, Ratings, Comments
from .forms import CommentForm

# Create your views here.
def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'review/home.html', {'restaurants': restaurants})

def restro_detail(request, slug):
    restaurant = get_object_or_404(Restaurant, slug=slug)
    average_rating = Ratings.objects.filter(restro=restaurant).aggregate(Avg('rating'))['rating__avg']
    comments = Comments.objects.filter(restro=restaurant).order_by("-created_at")
    ratings = Ratings.objects.filter(restro=restaurant)
    comment_count = Comments.objects.filter(is_approved=True).count()

    if request.method == "POST":
        print("Received a POST request")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.restro = restaurant
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm(data=request.POST)
    print("About to render template")

    return render(request, 'review/restro_detail.html', {
        'restaurant': restaurant, 
        'average_rating': average_rating, 
        'comments': comments, 
        'ratings': ratings,
        'comment_count': comment_count,
        'comment_form': comment_form,
    })