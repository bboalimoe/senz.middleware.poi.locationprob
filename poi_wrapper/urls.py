from django.conf.urls import patterns, include, url

urlpatterns = patterns('poi_wrapper.views.location_prob',
                       url(r'^locationprob/$', 'location_prob'),)