# -*- coding : utf-8 -*-
"""pystagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from photo import views

# As of Django 1.10, the patterns module has been removed (it had been deprecated since 1.8).
# just write url patterns directly
# Django 1.8

urlpatterns = [
        url(r'^photo/$', views.single_photo, name='view_single_photo'),
        url(r'^admin/', admin.site.urls),
]
