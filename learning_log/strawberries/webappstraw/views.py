from django.shortcuts import render

def catalog(request):
    return render(request, 'learning_log/strawberries/templates/main.html')

def profile(request):
    return render(request, '')

def login(request):
    return render(request, 'learning_log/strawberries/templates/login.html')

def signin(request):
    return render(request, 'learning_log/strawberries/templates/register.html')

