from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pruthvi_dot_me.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^robots.txt', TemplateView.as_view(template_name='robots.txt')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', include('about.urls')),
    url(r'^dreamer/', include('dreamer.urls')),
    url(r'^creator/', include('creator.urls')),
    url(r'^momentographer/', include('momentographer.urls')),
    url(r'^happenings/', include('happenings.urls')),

    #below static line is very important for media files, and has to be here: main url
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
