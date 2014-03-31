# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Forum ( models.Model ) :
    
    slug  = models.SlugField()
    name  = models.CharField( max_length = 255 )
    group = models.CharField( max_length = 255, blank = True )


    class Meta:
        
        ordering = ['group']


    def __unicode__ ( self ) :
        
        return self.name



class Topic ( models.Model ) :
    
    forum   = models.ForeignKey( Forum )
    subject = models.CharField( max_length = 255 )
    created = models.DateTimeField( auto_now_add = True )


    class Meta:
        
        ordering = ['id']
        

    def __unicode__(self):
        
        return self.subject
    
    

class ArticleManager( models.Manager ) :
    
    pass 
    

class Article ( models.Model ) :
    
    topic   = models.ForeignKey( Topic )
    text    = models.TextField()
    filter  = models.CharField( max_length = 50 )
    created = models.DateTimeField( auto_now_add = True )
    author  = models.ForeignKey( User )


    class Meta:
        
        ordering = ['id']


    def __unicode__ ( self ) :
        
        return '( %s, %s, %s )' % ( self.topic, self.author, self.created.replace( microsecond = 0 ) )


    def html ( self ) :
        '''
        Возвращает HTML-текст статьи, полученный фильтрацией содержимого
        через указанный фильтр.
        '''
        # implement filtering
        return self.text