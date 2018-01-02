"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^index$', views.index,name="index_page"),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page,name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)/$', views.edit_page,name='edit_page'),
    url(r'^delete/(?P<article_id>[0-9]+)/$', views.delete_page,name='delete_page'),
    url(r'^edit_action/$', views.edit_action ,name='edit_action')
]
