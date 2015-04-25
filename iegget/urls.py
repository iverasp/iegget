from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iegget.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.blog.urls')),
    url(r'^auth/', include('apps.userauth.urls')),
    url(r'^file/', include('apps.file.urls')),
    url(r'', include('two_factor.urls', 'two_factor')),
)

from wiki.urls import get_pattern as get_wiki_pattern
from django_nyt.urls import get_pattern as get_nyt_pattern
urlpatterns += patterns('',
    (r'^notifications/', get_nyt_pattern()),
    (r'^wiki/', get_wiki_pattern())
)
