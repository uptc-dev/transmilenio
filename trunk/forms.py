from __future__ import unicode_literals
from django import forms
from .models import Trunk


class TrunkForm(forms.ModelForm):
    class Meta:
        model = Trunk
        fields = [
            'first_letter',
            'name',
            'hex_color',
            'trunk_lenght',
            'pre_trunk_lenght',
        ]
