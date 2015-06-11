from django.conf import settings
import django.contrib.auth
from django.contrib.auth import authenticate, login, logout
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect, Http404
from homepage import models
import random
from django import forms
import string


templater = get_renderer('homepage')

@view_function
def process_request(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = django.contrib.auth.authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                django.contrib.auth.login(request, user)
            return HttpResponseRedirect('/homepage/getting_started/')


    template_vars = {
        'form': form,
    }

    return templater.render_to_response(request, 'login.html', template_vars)


@view_function
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/homepage/')



class LoginForm(forms.Form):

    email = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(required=True, min_length=8, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        self.user = django.contrib.auth.authenticate(username=email, password=password)
        print(self.user)
        if self.user == None:
            raise forms.ValidationError('Incorrect username/password.')

        return self.cleaned_data
