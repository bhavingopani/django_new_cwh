from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

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
    return HttpResponse("This is about page") 
def services(request):
    return HttpResponse("This is services page")
def contact(request):
    return HttpResponse("This is contact page")