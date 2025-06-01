from django.shortcuts import render

def catalog(request):
    return render(request, '../templates/main.html')

def profile(request):
    return render(request, '')

def login(request):
    return render(request, '../templates/login.html')

def signin(request):
    return render(request, '../templates/register.html')

def basket(request):
    return 