"""pruthvi_dot_me URL Configuration

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
#1.8 might not require patterns from conf.urls

from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic.base import TemplateView
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^robots.txt', TemplateView.as_view(template_name='robots.txt')),
    url(r'^about/', include('about.urls')),
    url(r'^creator/', include('creator.urls')),
    url(r'^dreamer/', include('dreamer.urls')),
    url(r'^happenings/', include('happenings.urls')),
    url(r'^momentographer/', include('momentographer.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
