# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django import forms
from django.contrib.gis.geos import GEOSGeometry


from .models import ServiceArea


class ServiceAreaForm(forms.Form):
    """
        This form is to create service area, the field area is a charfield type to store the polygon values
        represented as srting and used to create a Geometry Value with the polygon values to assign the
        area field on the model
    """
    area = forms.CharField(max_length=2000, widget=forms.HiddenInput(), required=True)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ServiceAreaForm, self).__init__(*args, **kwargs)

    def save(self):
        area = self.cleaned_data.get('area')

        pnt = GEOSGeometry(area)

        instance = ServiceArea.objects.create(area=pnt, user=self.user)

        return instance
