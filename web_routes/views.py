from django.shortcuts import render, redirect, get_object_or_404
from .models import Review


def index(request):
    return render(request, 'index.html')

def review_view(request, id):
    review = get_object_or_404(Review, url_id=id)
    data = {
        'review': review
    }
    return render(request, 'review_view.html', data)

def review_list(request):
    reviews = Review.objects.all()
    data = {
        'reviews': reviews
    }
    return render(request, 'review_list.html', data)

def review_edit(request):
    if _authenticated(request):
        return render(request, 'review_edit.html')
    return redirect(sign_in)

def review_new(request):
    if _authenticated(request):
        return render(request, 'review_new.html')
    return redirect(sign_in)

def sign_in(request):
    if _authenticated(request):
        return redirect(index)
    return render(request, 'sign_in.html')

def sign_up(request):
    if _authenticated(request):
        return redirect(index)
    return render(request, 'sign_up.html')


def _authenticated(request):
    if request.user.is_authenticated:
        return True
    return False
