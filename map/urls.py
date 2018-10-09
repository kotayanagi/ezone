from django.urls import include, path
from . import views



urlpatterns = [
    path('', views.miyagi, name='home'),
    path('about', views.about, name='about'),
    path('price', views.price, name='price'),
    path('contact', views.contact, name='contact'),
]