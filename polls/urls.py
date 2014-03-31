# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns('polls.views',
                       
    url( r'^$', 'IndexView.as_view()', name = 'index' ),
    url( r'(?P<pk>\d+)/$', 'DetailView.as_view()', name = 'detail' ),
    url( r'(?P<pk>\d+)/results/$', 'ResultsView.as_view()', name = 'results' ),
    url( r'(?P<pk>\d+)/vote/$', 'vote', name = 'vote' ),
)
