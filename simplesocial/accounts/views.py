from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import login, logout


from django.views.generic import TemplateView, CreateView
from . import forms
# Create your views here.



class SignUpView(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = "accounts/signup.html"
