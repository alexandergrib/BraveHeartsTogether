from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.add_story, name='stories'),
    path('add_story/', views.add_story, name='add_story')
]