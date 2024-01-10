from django.urls import path
from .views import *
urlpatterns = [
        path("", myfunction, name='main'),
        path("about/", myabout, name='about'),
        path("login/", mylogin, name='login'),
        path("contact/", mycontact, name='contact'),
        path("registration/", myregistration, name='registration'),

]