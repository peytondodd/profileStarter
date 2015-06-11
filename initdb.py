#!/usr/bin/env python 3

# initialize django

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'profileStarter.settings'
import django
django.setup()

# #regular imports
import homepage.models as models
from django.db import connection
import subprocess, sys
#
cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")
#
# #create db
cursor.execute("CREATE SCHEMA PUBLIC")
#
# #Migrage db
subprocess.call([sys.executable, "manage.py", "syncdb"])

# #Delete old Student users
models.User.objects.all().delete()
