"""healthcare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url, include
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

schema_view = get_swagger_view(title='CLC - Live - Healthcare')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', schema_view),
    url(r'^api-auth/', include('rest_framework.urls')),
    url('api/healthcare/', include('address.address_router')),
    url('api/healthcare/', include('doctor.doctor_router')),
    url('api/healthcare/', include('hospital.hospital_router')),
    url('api/healthcare/', include('patient.patient_router')),
    url(r'^get-api-token', views.obtain_auth_token, name='api-token'),

    url(r'^auth-jwt/', obtain_jwt_token),
    url(r'^auth-jwt-refresh/', refresh_jwt_token),
    url(r'^auth-jwt-verify/', verify_jwt_token),


]
