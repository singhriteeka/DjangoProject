from django.shortcuts import render

# Create your views here.
def landing_view(request):
    return render (request,'base.html')
def home_view(request):
    return render (request,'pages/home.html')
def about_view(request):
    return render (request,'pages/about.html')
def career_view(request):
    return render (request,'pages/career.html')
def contact_view(request):
    return render (request,'pages/contact.html')


