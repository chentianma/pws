"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.blogHome),
    url(r'^index/$', views.blogIndex),
    url(r'^about/$', views.blogAbout),
    url(r'^message/$', views.blogMessage),
    url(r'^article/(?P<pk>[0-9]+)/$', views.blogArticle, name='article'),
    url(r'^new/$', views.blogNew),
    url(r'^article/edit/(?P<pk>[0-9]+)/$', views.blogEdit, name='article_edit'),
]
