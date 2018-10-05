# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import Zone

@admin.register(Zone)
class ZoneCompany(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'sector',
    )
