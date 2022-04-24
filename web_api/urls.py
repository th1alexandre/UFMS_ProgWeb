from django.urls import path
from web_api import views


urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('user-create', views.user_create, name='user_create'),
    path('user-delete', views.user_delete, name='user_delete'),
    path('user-update', views.user_update, name='user_update'),
]
