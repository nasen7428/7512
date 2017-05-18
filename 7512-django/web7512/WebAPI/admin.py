# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from WebAPI.models import Node,User,Space

# Register your models here.

admin.site.register([Node,User,Space])
