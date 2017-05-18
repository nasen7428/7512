# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from WebAPI.models import Node,User,Space

class ContactAdmin(admin.ModelAdmin):
	list_display=('id','id')

# Register your models here.
admin.site.register([Node,User,Space],ContactAdmin)
