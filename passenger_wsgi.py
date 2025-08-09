# passenger_wsgi.py

import os
import sys

# Point to your actual project path
sys.path.insert(0, '/home/pldassociationor/pld_backend')
sys.path.insert(0, '/home/pldassociationor/virtualenv/pld_backend/3.10/lib/python3.10/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = 'pld.settings.prod'  # Or 'pld.settings' if not using prod

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# import sys, os

# sys.path.insert(0, '/home/username/projectname')
# sys.path.insert(1, '/home/username/projectname/pld')

# os.environ['DJANGO_SETTINGS_MODULE'] = 'pld.settings.prod'

# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()
