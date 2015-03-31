try:
    from django.conf.urls import include, patterns, url
except ImportError:
    from django.conf.urls.defaults import include, patterns, url
from django.contrib import admin

urlpatterns = patterns(
    'apps.blog.views',
    url(r'^$', 'index', name='index'),
    url(r'^about/', 'about', name='about'),
)
