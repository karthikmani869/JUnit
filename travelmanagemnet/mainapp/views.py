from django.shortcuts import render

# Create your views here.
def myfunction(request):
    return render(request, "mainpage.html")
def myabout(request):
    return render(request, "about.html")
def mylogin(request):
    return render(request, "login.html")
def myregistration(request):
    return render(request, "registration.html")
def mycontact(request):
    return render(request, "contact.html")