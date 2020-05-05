from django.urls import path

from . import views

app_name = "kanban"

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),  # Add home
    path('signup/', views.signup, name='signup'),  # Add signup
    path("users/<int:pk>/", views.UserDetailView.as_view(), name="users_detail"),  # pk=primary key like ID
]
