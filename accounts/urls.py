
from django.urls import path, include
from accounts import views

urlpatterns = [

    path('', views.account, name='account'),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name='logout'),
    path('register_user/', views.register_user, name="register_user"),
    # path('notRegistered/', views.notRegistered, name="notRegistered"),
    # path('edit/<profile_id/>', views.profileEdit, name='edit_user'),
    # path('delete/<profile_id/>', views.profileDelete, name='delete_user'),
]