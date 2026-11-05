from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return render(request,'home.html')
def product_view(request):
    return render(request,'product.html')
def exit_view(request):
    return render(request,'exit.html')