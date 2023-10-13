from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    # ... Other URLs

    # User Registration
    path('register/', views.register, name='register'),

    # User Login
    path('login/', views.user_login, name='login'),

    # Create Task
    path('create/', views.create_task, name='task-create'),
    path('', views.task_list, name='task-list'),
    path('detail/<int:task_id>/', views.task_detail, name='task-detail'),

    path('edit/<int:task_id>/', views.edit_task, name='task-edit'),


    # User Logout
    path('logout/', views.user_logout, name='logout'),
   
]
