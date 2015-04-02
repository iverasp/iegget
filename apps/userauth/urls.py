try:
    from django.conf.urls import include, patterns, url
except ImportError:
    from django.conf.urls.defaults import include, patterns, url
from django.contrib import admin

urlpatterns = patterns(
    'apps.userauth.views',
    url(r'^login/', 'login_user', name='login_user'),
    url(r'^logout/', 'logout_user', name='logout_user'),
)
