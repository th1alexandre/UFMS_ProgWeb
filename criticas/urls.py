from django.urls import path
from criticas import views

urlpatterns = [
    path('', views.index, name='index')
]
