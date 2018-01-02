# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','publish_time')
    list_filter = ('publish_time',)

# Register your models here.
admin.site.register(models.Article,ArticleAdmin)
