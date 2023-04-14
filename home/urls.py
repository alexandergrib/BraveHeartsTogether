from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('register_user', views.register_user, name="register_user"),
    path('login', views.login_user, name="login"),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('account/', views.account, name='account'),
]
