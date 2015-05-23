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

    template_vars = {
    }

    return templater.render_to_response(request, 'index.html', template_vars)

@view_function
def signup(request):

    form = SignupForm()
    user = models.User()


    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        print('###############################checks form############################### ')
        if form.is_valid():

            user.username = form.cleaned_data['email']
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password1'])
            user.save()
            print(user)
            print('###############################created############################### ')

            return HttpResponse('''
            <script>
                window.location.href = window.location.href;
            </script>
            ''')


    template_vars = {
        'form': form,
    }



    return templater.render_to_response(request, 'index.signup.html', template_vars)

class SignupForm(forms.Form):

    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(required=True, min_length=8, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(required=True, min_length=8, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean_email(self):
        user = models.User.objects.filter(email=self.cleaned_data['email'])
        print(user.count())
        if user.count() > 0:
            print("Account already created")
            raise forms.ValidationError("You've already created an account")
        return self.cleaned_data['email']


    # Validate - 1+ Numbers, 1+ Letters
    def clean_password (self):
        # Setup Our Lists of Characters and Numbers
        characters = dict.fromkeys(string.ascii_letters, 0)
        numbers = [str(i) for i in range(10)]

        value = self.cleaned_data['password1']

        # Assume False until Proven Otherwise
        numCheck = False
        charCheck = False

        # Loop until we Match
        for char in value:
            if not charCheck:
                if char in characters:
                    charCheck = True
            if not numCheck:
                if char in numbers:
                    numCheck = True
            if numCheck and charCheck:
                break

        if not numCheck or not charCheck:
            raise forms.ValidationError(u'Your password must include at least \
                                          one letter and at least one number.')

        return self.cleaned_data['password1']

    def clean_password2 (self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("Oooops! It looks like your passwords don't match")
        return self.cleaned_data['password2']
