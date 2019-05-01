"""tekey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include
from django.contrib import admin
try:
    from django.urls import re_path as url
except ImportError:
    from django.conf.urls import url


from tapp.views import FooView

urlpatterns = [
    url('admin/', admin.site.urls),
    url('foo/(?P<slug>[0-9a-zA-Z-_=]+)/$', FooView.as_view(), name='foo'),
]
