from django.shortcuts import render
def myfunc(request):
    return render(request, "index.html")
# Create your views here.

def myfunction2(request):
    return render(request,'travel.html')