from django.conf.urls import patterns, include, url
from happenings import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pruthvi_dot_me.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[\w\-]+)/$', views.post, name='post'),
    
)
