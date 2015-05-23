from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.http import HttpResponse, HttpResponseRedirect, Http404



class User(AbstractUser):
    school = models.CharField(max_length=300, blank=True, null=True)
    job = models.BooleanField(default=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=12, blank=True, null=True)
    zip_code = models.IntegerField( blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
