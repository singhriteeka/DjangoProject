from django.shortcuts import render


def main_view(request):
    return render(request, 'main.html')


def login_view(request):
    return render(request, 'pages/login.html')


def signup_view(request):
    return render(request, 'pages/signup.html')