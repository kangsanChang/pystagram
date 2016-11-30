# coding : utf-8
#-*- coding: utf-8-*-
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
# url 의 views부분에 views.single_photo바로 적는다.
from photo import views
# url 의 views부분에 photo.views.single_photo라고 적어준다.
# import photo.views

# As of Django 1.10, the patterns module has been removed (it had been deprecated since 1.8).
# just write url patterns directly

# url 함수는 regex,view,name,kwargs 총4개의 인자를 받는데 이중 regex와 view는 필수이다.
# django 이전 버전에서는 view 부분을 string 으로 적엇는데 이젠 그냥 적어준다.
# name 인자는 template에서 url연결자 이름으로 주소를 출력하는 등의 편의에 쓰인다.

urlpatterns = [
        url(r'^photo/(?P<photo_id>\d+)$', views.single_photo, name='view_single_photo'),
        url(r'^admin/', admin.site.urls),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static('static_files', document_root=settings.MEDIA_ROOT)
