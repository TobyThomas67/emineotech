from datetime import datetime
from django.shortcuts import render

from .models import Image

# Create your views here.
def home_page(request):
    today = datetime.now()
    day_of_cycle = (today.day - 1) % 1  # Ensure it wraps every 10 days

    # Get 5 images for the current day (5 images per day)
    start_index = day_of_cycle * 5
    images_for_today = Image.objects.all()[start_index:start_index + 5]

    return render(request, 'index.html', {'images': images_for_today})
    
def contact_page(request):
    today = datetime.now()
    day_of_cycle = (today.day - 1) % 1  # Ensure it wraps every 10 days

    # Get 5 images for the current day (5 images per day)
    start_index = day_of_cycle * 5
    images_for_today = Image.objects.all()[start_index:start_index + 5]

    return render(request, 'contact.html', {'images': images_for_today})

def about_page(request):
    today = datetime.now()
    day_of_cycle = (today.day - 1) % 1  # Ensure it wraps every 10 days

    # Get 5 images for the current day (5 images per day)
    start_index = day_of_cycle * 5
    images_for_today = Image.objects.all()[start_index:start_index + 5]

    return render(request, 'about.html', {'images': images_for_today})

def services_page(request):
    # Get today's date and calculate the "day number" (1-10)
    today = datetime.now()
    day_of_cycle = (today.day - 1) % 1  # Ensure it wraps every 10 days

    # Get 5 images for the current day (5 images per day)
    start_index = day_of_cycle * 5
    images_for_today = Image.objects.all()[start_index:start_index + 5]

    return render(request, 'services.html', {'images': images_for_today})

def carousel_view(request):
    # Get today's date and calculate the "day number" (1-10)
    today = datetime.now()
    day_of_cycle = (today.day - 1) % 1  # Ensure it wraps every 10 days

    # Get 5 images for the current day (5 images per day)
    start_index = day_of_cycle * 5
    images_for_today = Image.objects.all()[start_index:start_index + 5]

    return render(request, 'carousel.html', {'images': images_for_today})