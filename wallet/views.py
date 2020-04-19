from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Shylockentry
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

# class-based views


class EntryListView(LoginRequiredMixin, ListView):
    model = Shylockentry
    template_name = "wallet/home.html"
    context_object_name = "entries"
    login_url = '/users/login'

    def get_context_data(self, *args, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # changing the context implementation to get entries of only the user
        context = {"entries": Shylockentry.objects.filter(
            user_id=self.request.user.id)}

        return context


class EntryCreateView(LoginRequiredMixin,  CreateView):
    model = Shylockentry
    fields = ["name", "amount", "type_choice", "deadline"]
    template_name = "wallet/add.html"
    success_url = '/wallet/'
    login_url = '/users/login'
    # redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.user = self.request.user
        type = form.cleaned_data['type_choice']

        if type == "D":
            messages.success(self.request, f'New debtor added!')
        elif type == "C":
            messages.success(self.request, f'New creditor added!')
        return super().form_valid(form)


class EntryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Shylockentry
    fields = ["name", "amount", "type_choice", "deadline"]
    template_name = "wallet/edit.html"
    success_url = '/wallet/'
    login_url = '/users/login'
    redirect_field_name = "/"

    def test_func(self):
        entry = self.get_object()
        if self.request.user == entry.user:
            return True
        messages.error(
            self.request, "You are not eligible to edit that entry.")
        return False

    # def get_login_url():
    #     return "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        type = form.cleaned_data['type_choice']
        name = form.cleaned_data['name']
        if type == "D":
            messages.success(self.request, f'{name}"s debt has been updated')
        elif type == "C":
            messages.success(
                self.request, f'{name}"s credit has been updated')

        return super().form_valid(form)


class EntryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Shylockentry
    fields = ["name", "amount", "type_choice", "deadline"]
    template_name = "wallet/delete.html"
    success_url = '/wallet/'
    login_url = '/users/login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        entry = self.get_object()
        if self.request.user == entry.user:
            return True
        messages.error(
            self.request, "You are not eligible to delete that entry.")
        return False


# functional views

# def home(request):
#     print(request.user.id)
#     return render(request, 'wallet/home.html')


# def add(request):
#     return render(request, 'wallet/add.html')


# def edit(request):
#     return render(request, 'wallet/edit.html')


def sample(request):
    return render(request, 'wallet/sample.html')
