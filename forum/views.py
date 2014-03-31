# -*- coding:utf-8 -*-

from django.shortcuts import get_object_or_404
from django.views.generic.list_detail import object_list

from forum.models import Forum, Topic, Article


def forum ( request, slug, **kwargs ) :
    
    forum = get_object_or_404( Forum, slug = slug )
    kwargs['queryset'] = forum.topic_set.all()
    kwargs['extra_context'] = { 'forum': forum }
    
    return object_list( request, **kwargs )


def topic ( request, slug, id, **kwargs ) :
    
    topic = get_object_or_404 (Topic, forum__slug = slug, id = id )
    kwargs['queryset'] = topic.article_set.all()
    kwargs['extra_context'] = { 'topic': topic, 'forum': topic.forum }
    
    return object_list(request, **kwargs)
