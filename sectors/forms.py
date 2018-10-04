from __future__ import unicode_literals
from django import forms
from .models import Sector


class SectorForm(forms.ModelForm):
    class Meta:
        model = Sector
        fields = [
            'name',
        ]
