# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic.list_detail import object_list

from core import settings
from forum.models import Forum, Topic, Article


info = {
    'paginate_by': settings.PAGINATE_BY,
    'allow_empty': True,
}

urlpatterns = patterns( 'forum.views',
    
    url( r'^$', object_list, { 'queryset' : Forum.objects.all() } ),
    url( r'^([a-z0-9-]+)/$', 'forum', info ),
    url( r'^([a-z0-9-]+)/(\d+)/$', 'topic', info),
)