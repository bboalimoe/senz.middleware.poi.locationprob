from django.conf.urls import patterns, include, url
from django.contrib import admin

from poi_wrapper import urls as senz_urls


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^senz/', include(senz_urls))
)
