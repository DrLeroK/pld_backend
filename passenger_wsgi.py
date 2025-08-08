# passenger_wsgi.py

import sys, os

sys.path.insert(0, '/home/username/projectname')
sys.path.insert(1, '/home/username/projectname/pld')

os.environ['DJANGO_SETTINGS_MODULE'] = 'pld.settings.prod'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
