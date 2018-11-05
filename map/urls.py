from django.urls import include, path
from . import views



urlpatterns = [
    path('', views.top, name='top'),
    path('e-zone', views.pref, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]