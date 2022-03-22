from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from home.models import Contact   #importing Contact module from models.
import datetime         #importing date and time model to use here

# Create your views here.
def index(request):
    # return HttpResponse("This is homepage")  #we are using HttpResponse as its just string that we want to directly print
                                            #IDEALLY we should NOT USE HttpResponse --  ALWAYS USE TEMPLATE
    context = {
        "variable1": "this is sent",  #this is how we send variable to view from here.
        "variable2": "this is also sent" 
    }
        #this is not how we send variable -- ideal way is the fetch the value or data from model and then send it to view.

    return render(request, "index.html", context) #the first argument is request and the second argument is the NAME OF THE TEMPLATE , then context and variable list - context here is also called python dictioneries

#now creating a differnt pages for our business for sample

def about(request):
    # return HttpResponse("This is about page") 
    return render(request, "about.html")  #rendering templates instead of http response. -- we did not write context as we are not sending any variable
def services(request):
    # return HttpResponse("This is services page")
    return render(request, "services.html")  #rendering templates instead of http response. -- we did not write context as we are not sending any variable
def contact(request):
    # return HttpResponse("This is contact page")
    #logic to add entry into db
    if request.method == "POST":
        name = request.POST.get('name') #request.POST is the dictionery and get is the method we used to get the name
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date= datetime.today())   WHY??? He is explaining check.
        contact.save()
    return render(request, "contact.html")  #rendering templates instead of http response. -- we did not write context as we are not sending any variable
