from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView

from .forms import UserForm
from .mixins import OnlyYouMixin

# Create your views here.


class UserDetailView(LoginRequiredMixin, DetailView):  # only for the logged in user
    model = User
    template_name = "kanban/users/detail.html"


class UserUpdateView(OnlyYouMixin, UpdateView):  # only for the logged in user
    model = User
    template_name = "kanban/users/update.html"
    form_class = UserForm

    def get_success_url(self):
        return resolve_url('kanban:users_detail', pk=self.kwargs['pk'])


def index(request):
    return render(request, "kanban/index.html")


def home(request):
    return render(request, "kanban/home.html")


# Sign Up
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_instance = form.save()
            login(request, user_instance)
            return redirect("kanban:home")
    else:
        form = UserCreationForm()

    context = {
        "form": form
    }
    return render(request, 'kanban/signup.html', context)

# Login Decorator
@login_required
def home(request):
    return render(request, "kanban/home.html")
