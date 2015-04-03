try:
    from django.conf.urls import include, patterns, url
except ImportError:
    from django.conf.urls.defaults import include, patterns, url
from django.contrib import admin

urlpatterns = patterns(
    'apps.file.views',
    url(r'^$', 'index', name='index'),
    url(r'^upload/', 'upload', name='upload'),
    url(r'^get/(?P<uuid>[^/]+)/$', 'get', name='get'),

)
