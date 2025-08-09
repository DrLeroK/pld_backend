import os
from .base import *

# Security
DEBUG = False
# ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com', 'api.yourdomain.com']
ALLOWED_HOSTS = ['*']
SECRET_KEY = os.environ['SECRET_KEY']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Static files (replace with your actual domain)
STATIC_URL = '/static/'
STATIC_ROOT = '/home/pldassociationor/public_html/static'  # cPanel serves from here
STATICFILES_DIRS = [BASE_DIR / 'static']  # Your local static files

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/pldassociationor/public_html/media'  # cPanel-compatible path


# STATIC_ROOT = '/home/pldassociationor/pld_backend/staticfiles/'
# MEDIA_ROOT = '/home/pldassociationor/pld_backend/mediafiles/'

# Security headers
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# CORS - restrict to your frontend domain
# CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOWED_ORIGINS = [
#     "https://yourdomain.com",
#     "https://www.yourdomain.com",
#     "https://your-vercel-app.vercel.app",
# ]


# Email - use real SMTP in production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


















# # pld/settings/prod.py

# import os
# from .base import *


# DEBUG = False
# ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com', 'server-ip-address']


# STATIC_ROOT = '/home/username/projectname/static'
# MEDIA_ROOT = '/home/username/projectname/media'


# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True


# # PostgreSQL
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('DB_NAME'),
#         'USER': os.getenv('DB_USER'),
#         'PASSWORD': os.getenv('DB_PASS'),
#         'HOST': os.getenv('DB_HOST', 'localhost'),
#         'PORT': os.getenv('DB_PORT', '5432'),
#     }
# }

# CORS_ALLOW_ALL_ORIGINS = True  # Disable in prod
# # CORS_ALLOWED_ORIGINS = [
# #     "https://yourdomain.com",
# #     "https://www.yourdomain.com",
# # ]