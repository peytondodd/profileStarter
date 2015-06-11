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
from localflavor.us.forms import USPhoneNumberField
from localflavor.us.forms import USStateSelect
from localflavor.us.us_states import US_STATES as states

import string


templater = get_renderer('homepage')

@view_function
def process_request(request):

    user = models.User.objects.get(id=request.user.id)


    form = ProfileForm()
    if request.method == 'POST':
        print('post')
        form = ProfileForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first']
            user.last_name= form.cleaned_data['last']
            user.job_or_internship = form.cleaned_data['job_or_internship']
            user.phone= form.cleaned_data['phone_number']
            user.gender= form.cleaned_data['gender']
            user.hometown= form.cleaned_data['hometown']
            user.state= form.cleaned_data['state']
            user.school= form.cleaned_data['school']
            user.start_year= form.cleaned_data['start_year']
            user.graduation_year = form.cleaned_data['graduation_year']
            user.degree = form.cleaned_data['degree']
            user.major = form.cleaned_data['major']
            user.minor = form.cleaned_data['minor']
            user.gpa = form.cleaned_data['gpa']
            user.why_im_awesome = form.cleaned_data['why_im_awesome']

            user.save()
            print(user)


            print('valid form')


            return HttpResponseRedirect('/homepage/')

    template_vars = {
        'form': form,
    }


    return templater.render_to_response(request, 'complete_profile.html', template_vars)







class ProfileForm(forms.Form):

    GENDER_CHOICES = (
        ('Male','Male'),('Female','Female'),
    )

    START_YEAR_CHOICES = (
        ('2015', '2015'),
        ('2014', '2014'),
        ('2013', '2013'),
        ('2012', '2012'),
        ('2011', '2011'),
        ('2010', '2010'),
        ('2009', '2009'),
        ('2008', '2008'),
        ('2007', '2007'),
        ('2006', '2006'),
        ('2005', '2005'),
        ('2004', '2004'),
        ('2003', '2003'),
        ('2002', '2002'),
        ('2001', '2001'),
        ('2000', '2000'),
    )

    GRADUATION_YEAR_CHOICES = (
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
        ('2022', '2022'),
        ('2023', '2023'),

    )

    JOB_OR_INTERNSHIP = (
        ('Internship', 'Internship'),
        ('Job', 'Job'),
        ('Both', 'Both'),
    )

    DEGREE = (
        ('Associates','Associates'),
        ('Bachelors','Bachelor'),
        ('Master','Master'),
        ('Doctorate','Doctorate'),
        ('Other','Other'),
    )


    first = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your first name here'}))
    last = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your last name'}))
    job_or_internship = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=JOB_OR_INTERNSHIP)
    phone_number = USPhoneNumberField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'XXX-XXX-XXXX'}))
    gender = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=GENDER_CHOICES, label='Gender')
    hometown = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your hometown'}))
    state = forms.ChoiceField(widget=USStateSelect(attrs={'class':'form-control'}),choices=states,label='homestate')
    school = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'the school you go to'}))
    start_year = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=START_YEAR_CHOICES)
    graduation_year = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=GRADUATION_YEAR_CHOICES)
    degree = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=DEGREE)
    major = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Major'}))
    minor = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Minor'}))
    gpa = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'hidden-gpa','id':'gpa-value','name':'gpa'}))
    why_im_awesome = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'tell us why other people enjoy working with you'}))
