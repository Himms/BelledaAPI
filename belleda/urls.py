"""belleda URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from django import urls
# from django.urls.conf import include
# # from belleda import belleda_main
# from django.conf import settings
# from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from BelledaAPIapp.views import RegistrationAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="Belleda Fashion App",
      default_version='v1',
      description="A cross-platform application that connects fashion designers and clients for the purpose of creating and selling fashion items.",
      terms_of_service="https://www.zuri.com/terms/",
      contact=openapi.Contact(email="siegfredsamson@gmail.com"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('designers/', include('designer.urls')),
    # path('', include('belleda_main.urls')),
    path('api/v1/', include('BelledaAPIapp.urls')),
    # path('api/v1/auth/auth-token', obtain_auth_token, name='obtain-auth-token'),
    path('auth/register/', RegistrationAPIView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/refresh-token', TokenRefreshView.as_view(), name='refreshtoken'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
  
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
