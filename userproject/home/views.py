from django.shortcuts import render, redirect  #redirect added mannually
from django.contrib.auth.models import User #added by me
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") #return to login if the the user is anonymous. Otherwise go home page.
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password) #checking if the username of pass gets printed or not.
        # check if user has entered correct credentials
        #authentication username and password
        user = authenticate(username=username, password=password)
        if user is not None:
        # A backend authenticated the credentials
            login(request, user) 
            return redirect("/")  #redirecting to home page if credentials are correct
        else:
        # No backend authenticated the credentials
            return render(request, 'login.html') #redirecting to login page again if credentials are wrong.
    return render(request, 'login.html')
def logoutUser(request):
    logout(request)
    return redirect("/login")  #here we are redirecting user to home page or index.html when they logout



