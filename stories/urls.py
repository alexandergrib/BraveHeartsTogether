from django.urls import path
from stories import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.stories, name='stories'),
    path('add_story/', views.add_story, name='add_story'),
    path('edit_story/<int:story_id>', views.edit_story, name='edit_story')
]
