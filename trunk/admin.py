from django.contrib import admin

from .models import Trunk


@admin.register(Trunk)
class TrunkCompany(admin.ModelAdmin):
    list_display = (
        'pk',
        'first_letter',
        'name',
        'hex_color',
        'trunk_lenght',
        'pre_trunk_lenght',
    )
