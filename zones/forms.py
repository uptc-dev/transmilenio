from __future__ import unicode_literals
from django import forms
from .models import Zone


class ZoneForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = [
            'name',
            'sector',
            'trunk',
        ]
