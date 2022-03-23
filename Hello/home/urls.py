from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    #REMOVED path('admin/', admin.site.urls), #this means whoever comes and do /admin   then it will go to Django Admin page - already from the Hello urls.py file.
    path("", views.index, name= 'home'), #this means whoever comes with blank path then .. send them to views index function and Give name to path - home

    path("about", views.about, name= 'about'), # means   slash  /about  will lead to views.about function

    path("services", views.services, name= 'services'),

    path("contact", views.contact, name= 'contact')
]
