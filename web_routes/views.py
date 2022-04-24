from django.shortcuts import render


def index(request):
    return render(request, 'index/index.html')

def review_(request):
    return render(request, 'review_/review_.html')

def review_edit(request):
    return render(request, 'review_edit/review_edit.html')

def review_new(request):
    return render(request, 'review_new/review_new.html')

def sign_in(request):
    return render(request, 'sign_in/sign_in.html')

def sign_up(request):
    return render(request, 'sign_up/sign_up.html')
