from django.conf import settings
import django.contrib.auth
from django.contrib.auth import authenticate, login, logout
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect, Http404
import random
from django import forms


templater = get_renderer('homepage')

@view_function
def process_request(request):

    template_vars = {
    }

    return templater.render_to_response(request, 'index.html', template_vars)

@view_function
def signup(request):
    template_vars = {}




    return templater.render_to_response(request, 'index.sighnup.html', template_vars)
