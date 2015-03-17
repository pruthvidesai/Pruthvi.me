from django.conf.urls import patterns, include, url
from momentographer import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pruthvi_dot_me.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),

)