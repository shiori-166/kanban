from django.urls import path

from . import views

app_name = "kanban"

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),  # Add home
    path('signup/', views.signup, name='signup'),  # Add signup
    path("users/<int:pk>/", views.UserDetailView.as_view(), name="users_detail"),  # pk=primary key like ID
    path("users/<int:pk>/update/", views.UserUpdateView.as_view(), name="users_update"),
    path("lists/", views.ListListView.as_view(), name="lists_list"),
    path("lists/create/", views.ListCreateView.as_view(), name="lists_create"),
    path("lists/<int:pk>/", views.ListDetailView.as_view(), name="lists_detail"),
]
