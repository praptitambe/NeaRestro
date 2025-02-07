from django.shortcuts import render, get_object_or_404, redirect
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
    comment_count = comments.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.restro = restaurant
            comment.save()
            return redirect('restro_detail', slug=slug)
    else:
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
            return redirect('restro_detail', slug=slug)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'review/edit_comment.html', {'form': form, 'restaurant': restaurant})

def comment_delete(request, slug, comment_id):
    restaurant = get_object_or_404(Restaurant, slug=slug)
    comment = get_object_or_404(Comments, id=comment_id, author=request.user)

    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
        return redirect('restro_detail', slug=slug)

    return render(request, 'review/restro_detail.html', {'restaurant': restaurant})