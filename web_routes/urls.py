from django.urls import path
from web_routes import views


urlpatterns = [
    path('', views.index, name='index'),
    path('review', views.review_view, name='review_view'),
    path('reviews', views.review_list, name='review_list'),
    path('review/edit', views.review_edit, name='review_edit'),
    path('review/new', views.review_new, name='review_new'),
    path('sign-in', views.sign_in, name='sign_in'),
    path('sign-up', views.sign_up, name='sign_up'),
]
