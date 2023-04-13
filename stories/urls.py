from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('stories/', views.add_story, name='add_story')
]