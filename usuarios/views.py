from django.shortcuts import render

def login(request):
    return render(request, 'login/login.html')

def create_user(request):
    return render(request, 'create_user/create.html')
