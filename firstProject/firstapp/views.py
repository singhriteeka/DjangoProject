from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login_view(request):
    return render(request,'login.html')
def signup_view(request):
    return render(request,'signup.html')
def landing_view(request):
    return render(request,'landing.html')
