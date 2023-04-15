
from django.urls import path, include
from accounts import views
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('account', views.account, name="account"),
    path('edit/<int:profile_id>/', views.profileEdit, name='edit_user'),
    path('delete/<int:profile_id>/', views.profileDelete, name='delete_user'),
    path('profile', views.profile, name='profile'),
]