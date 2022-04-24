from django.urls import path
from web_routes import views


urlpatterns = [
    path('', views.index, name='index'),
    path('review', views.review_, name='review_'),
    path('review/edit', views.review_edit, name='review_edit'),
    path('review/new', views.review_new, name='review_new'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
]
