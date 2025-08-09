import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pld.settings.prod')  # Match passenger_wsgi.py
application = get_wsgi_application()

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pld.settings')

# application = get_wsgi_application()
