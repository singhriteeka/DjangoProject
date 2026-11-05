from django.shortcuts import render

# Create your views here.
def about_view(request):
    return render(request,"about.html")
def home_view(request):
    return render(request,"home.html")
def career_view(request):
    return render(request,"career.html")
def contact_view(request):
    return render(request,"contact.html")