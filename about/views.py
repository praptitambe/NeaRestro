from django.shortcuts import render, redirect
from .models import About
from django.contrib import messages
from .forms import CollaborateForm


def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    if request.method == "POST":
        collaborate_form = CollaborateForm(request.POST, request.FILES)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request submitted successfully. We endeavour to respond within 2 working days.'
            )
            return redirect('about')
        
          
    return render(
        request,
        "about/about.html",
        {"about": about,
        "collaborate_form": collaborate_form },
    )