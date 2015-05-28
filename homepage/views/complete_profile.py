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
    form = ProfileForm()

    template_vars = {
        'form': form,
    }


    return templater.render_to_response(request, 'complete_profile.html', template_vars)





class ProfileForm(forms.Form):

    GENDER_CHOICES = (
        ('Male','M'),('Female','F'),
    )

    first = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your first name'}))
    last = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your last name'}))
    phone_number = forms.CharField(required=True,initial='4732817300654', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your phone 000-000-0000'}))
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES, label='Gender')
    hometown = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your hometown'}))
    state = forms.CharField(required=True,initial='Utah', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}))
    school = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'the school you go to'}))
    




    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        self.user = django.contrib.auth.authenticate(username=email, password=password)
        print(self.user)
        if self.user == None:
            raise forms.ValidationError('Incorrect username/password.')

        return self.cleaned_data
