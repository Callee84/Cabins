"""cabin URL Configuration

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
from django.contrib import admin
from django.urls import path, include

from cabin_web.views import (
    homePage
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cabin_web.urls'), name='cabin_web'),
    path('', homePage, name='home'),
    path('cabins_reservations/', include('cabins_reservations.urls')),
    path('guestbook/', include('guestbook.urls')),
    path('news/', include('news.urls')),
    path('contact/', include('contact.urls')),
    path('profiles/', include('django.contrib.auth.urls')),
    path('profiles/', include('profiles.urls')),
    path('accounts/', include('allauth.urls')),
    path('summernote/', include('django_summernote.urls')),
]
