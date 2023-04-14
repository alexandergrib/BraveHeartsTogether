
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account', views.account, name='account'),
    path('login', views.login_user, name="login"),
    path('register_user', views.register_user, name="register_user"),
    path('notRegistered', views.notRegistered, name="notRegistered"),
    path('edit/<profile_id>', views.profileEdit, name='edit'),
    path('delete/<profile_id>', views.profileDelete, name='delete'),
]