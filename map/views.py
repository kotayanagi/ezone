from django.shortcuts import render

from .models import Miyagi


def miyagi(request):
    miyagi_cities = Miyagi.objects
    #miyagi_city = get_object_or_404(Miyagi, pk=miyagi_id)
    return render(request, 'home.html', {'miyagi_cities':miyagi_cities}) #'miyagi_city':miyagi_city})

def about(request):
    return render(request, 'about.html', {})

def price(request):
    return render(request, 'price.html', {})

def contact(request):
    return render(request, 'contact.html', {})