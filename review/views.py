from django.shortcuts import render, get_object_or_404, reverse
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
            return HttpResponseRedirect(reverse('restro_detail', args=[slug]))

    comment_form = CommentForm()

    return render(request, 'review/restro_detail.html', {
        'restaurant': restaurant, 
        'comments': comments, 
        'comment_count': comment_count,
        'comment_form': comment_form,
    })


def comment_edit(request, slug, comment_id):
    restaurant = get_object_or_404(Restaurant, slug=slug)
    comment = get_object_or_404(Comments, id=comment_id, author=request.user)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Comment updated successfully!')
            return HttpResponseRedirect(reverse('restro_detail', args=[slug]))
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('restro_detail', args=[slug]))