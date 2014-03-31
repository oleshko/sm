# -*- coding: utf-8 -*-

from django.db import models



class Expert ( models.Model ) :
    
    last_name  = models.CharField( max_length = 30, verbose_name = u'Фамилия', null = True )
    first_name = models.CharField( max_length = 30, verbose_name = u'Имя', null = True )
    mid_name   = models.CharField( max_length = 30, verbose_name = u'Отчество', null = True )
    photo      = models.ImageField( upload_to = "img/experts", verbose_name = "Фото", blank = True, null = True )
    