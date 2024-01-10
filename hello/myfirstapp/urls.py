from django.urls import path
from .views import *

urlpatterns = [
    path("", myfunc),
    path('travel/',myfunction2,name='travel')
]