from django.urls import path
from web_routes import views


urlpatterns = [
    path('', views.index, name='index'),
    path('review', views.review_, name='review_'),
    path('review/edit', views.review_edit, name='review_edit'),
    path('review/new', views.review_new, name='review_new'),
    path('sign-in', views.sign_in, name='sign_in'),
    path('sign-up', views.sign_up, name='sign_up'),
]
