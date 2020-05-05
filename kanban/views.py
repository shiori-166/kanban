from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, ListView, DeleteView

from .forms import UserForm, ListForm, CardForm
from .mixins import OnlyYouMixin
from .models import List, Card

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


class ListCreateView(LoginRequiredMixin, CreateView):
    model = List
    template_name = "kanban/lists/create.html"
    form_class = ListForm
    success_url = reverse_lazy("kanban:lists_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ListListView(LoginRequiredMixin, ListView):
    model = List
    template_name = "kanban/lists/list.html"


class ListDetailView(LoginRequiredMixin, DetailView):
    model = List
    template_name = "kanban/lists/detail.html"


class ListUpdateView(LoginRequiredMixin, UpdateView):
    model = List
    template_name = "kanban/lists/update.html"
    form_class = ListForm

    def get_success_url(self):
        return resolve_url('kanban:lists_detail', pk=self.kwargs['pk'])


class ListDeleteView(LoginRequiredMixin, DeleteView):
    model = List
    template_name = "kanban/lists/delete.html"
    form_class = ListForm
    success_url = reverse_lazy("kanban:lists_list")


class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card
    template_name = "kanban/cards/create.html"
    form_class = CardForm
    success_url = reverse_lazy("kanban:home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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
