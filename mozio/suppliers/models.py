# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


@python_2_unicode_compatible
class ServiceArea(models.Model):
    """
        This model represents a service area, each service area is associated to a user(supplier), the area
        field represent a polygon area where user can define the service area.
    """
    area = models.PolygonField(_("Area"))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='service_areas')
    created = models.DateTimeField(_("Date Created"), auto_now_add=True, blank=True)
    objects = models.GeoManager()

    class Meta:
        get_latest_by = 'created'

    def __str__(self):
        return str(self.pk)
