from django.shortcuts import render, get_object_or_404,reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Restaurant, Comments
from .forms import CommentForm


# Create your views here.
def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'review/home.html', {'restaurants': restaurants})

def restro_detail(request, slug):
    restaurant = get_object_or_404(Restaurant, slug=slug)
    comments = Comments.objects.filter(restro=restaurant).order_by("-created_at")
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
        'comments': comments, 
        'comment_count': comment_count,
        'comment_form': comment_form,
    })


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Restaurant.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comments, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('restro_detail', args=[slug]))