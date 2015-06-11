# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.contrib.auth.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], verbose_name='username', max_length=30, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('job', models.BooleanField(default=True)),
                ('address', models.CharField(null=True, blank=True, max_length=60)),
                ('city', models.CharField(null=True, blank=True, max_length=30)),
                ('state', models.CharField(null=True, blank=True, max_length=12)),
                ('zip_code', models.IntegerField(null=True, blank=True)),
                ('phone', models.CharField(null=True, blank=True, max_length=30)),
                ('job_or_internship', models.CharField(null=True, blank=True, max_length=300)),
                ('gender', models.CharField(null=True, blank=True, max_length=300)),
                ('school', models.CharField(null=True, blank=True, max_length=300)),
                ('start_year', models.CharField(null=True, blank=True, max_length=300)),
                ('graduation_year', models.CharField(null=True, blank=True, max_length=300)),
                ('degree', models.CharField(null=True, blank=True, max_length=300)),
                ('major', models.CharField(null=True, blank=True, max_length=300)),
                ('minor', models.CharField(null=True, blank=True, max_length=300)),
                ('gpa', models.CharField(null=True, blank=True, max_length=300)),
                ('why_im_awesome', models.CharField(null=True, blank=True, max_length=300)),
                ('groups', models.ManyToManyField(blank=True, to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user', related_name='user_set', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, to='auth.Permission', help_text='Specific permissions for this user.', related_query_name='user', related_name='user_set', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
