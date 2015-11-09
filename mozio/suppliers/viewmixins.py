# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import geocoder


class LocationMixin(object):
    """
        This mixin setup map location according using IP address
    """

    def get_context_data(self, **kwargs):
        context = super(LocationMixin, self).get_context_data(**kwargs)
        visitor_ip = self.request.META.get('REMOTE_ADDR', None)
        latlng = {'lat': 37.774929, 'lng': -122.419416}
        if visitor_ip is not None:
            g = geocoder.ip(visitor_ip)
            if g.lat is not None and g.lng is not None:
                latlng.update(lat=g.lat, lng=g.lng)
        context['latlng'] = latlng
        return context
