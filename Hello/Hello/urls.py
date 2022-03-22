"""Hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


#added to change the django text
admin.site.site_header = "Amul Ice Cream Admin"
admin.site.site_title = "Amul Ice Cream Admin Portal"
admin.site.index_title = "Welcome to Amul Ice Cream"


urlpatterns = [
    path('admin/', admin.site.urls),  #this means whoever comes and do /admin   then it will go to Django Admin page
    path('', include('home.urls'))   #it means with this path.. or anything after / - he will be sent to home folder and urls file.   
    
]
