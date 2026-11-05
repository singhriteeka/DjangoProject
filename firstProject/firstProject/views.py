from django.http import HttpResponse

def name_view(request):
    return HttpResponse('<h1>I am Riteeka Singh</h1>')

def college_view(request):
    return HttpResponse('<h1>LIT</h1>')

def country_view(request):
    return HttpResponse('<h1>INDIA</h1>')

def login_view(request):
    return HttpResponse('<h1>LOGIN PAGE</h1>')

def signup_view(request):
    return HttpResponse('<h1>SIGNUP PAGE</h1>')