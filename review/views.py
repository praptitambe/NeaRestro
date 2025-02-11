from django.shortcuts import render, get_object_or_404, redirect,reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Restaurant, Comments
from .forms import CommentForm, RestroSearchForm
from django.db.models import Q
from django.core import serializers
from django.http import JsonResponse


# Create your views here.
def home(request):
    restaurants = Restaurant.objects.all()
    form = RestroSearchForm()
    q = ''
    c = ''
    results = []
    query = Q()

    if request.POST.get('action') == 'post':
        search_string = str(request.POST.get('ss'))

        if search_string is not None:
            search_string = Restaurant.objects.filter(
                name__icontains=search_string)[:5]

            data = serializers.serialize(
                'json', list(search_string), fields=('id', 'name', 'city')
            )
            print(data)
            return JsonResponse({'search_string': data})

    if 'q' in request.GET:
        form = RestroSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
            c = form.cleaned_data['c']

            if c is not None:
                query &= Q(cuisine__cuisine_type__icontains=c)
            if q is not None:
                query &= Q(Q(name__icontains=q) | Q(city__icontains=q))

            results = Restaurant.objects.filter(query)

    return render(request, 'review/home.html', {
        'form': form,
        'q': q,
        'c': c,
        'results': results,
        'restaurants': restaurants,
    })


def restro_detail(request, slug):
    restaurant = get_object_or_404(Restaurant, slug=slug)
    comments = Comments.objects.filter(restro=restaurant).order_by("-created_at")
    comment_count = comments.filter(is_approved=True).count()

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
    print(comments)
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
            messages.success(request, 'Comment updated successfully.')
            return redirect('restro_detail', slug=slug)
    else:
        form = CommentForm(instance=comment)

    return render(
        request, 'review/edit_comment.html', 
        {'form': form, 'restaurant': restaurant}
    )


def comment_delete(request, slug, comment_id):
    restaurant = get_object_or_404(Restaurant, slug=slug)
    comment = get_object_or_404(Comments, id=comment_id, author=request.user)
    if request.method == 'GET':
        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
        return redirect('restro_detail', slug=slug)

    return render(
        request, 'review/restro_detail.html', 
        {'restaurant': restaurant}
        )