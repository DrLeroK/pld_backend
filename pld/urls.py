"""
URL configuration for pld project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import RedirectView


schema_view = get_schema_view(
    openapi.Info(
        title="PLD Association Website",
        default_version='v1',
        description="API documentation for PLD Association",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # Redirect root URL to Swagger documentation
    path('', RedirectView.as_view(url='/swagger/')),

    # Admin
    path('admin/', admin.site.urls),


    # Products app
    path('core/', include('apps.core.urls')),

    # User management
    path('user_management/', include('apps.user_management.urls')),

    # Authentication (JWT)
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
    # Djoser endpoints for password reset
    path('auth/', include('djoser.urls')),  # Main Djoser endpoints
    path('auth/', include('djoser.urls.jwt')),  # JWT-specific endpoints
    

    # Documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

