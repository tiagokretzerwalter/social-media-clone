from django.shortcuts import render
from django.core.urlresolvers import reverselazy
from django.views.generic import CreateView
from . import forms

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverselazy('login')
    template_name = 'accounts/signup.html'
