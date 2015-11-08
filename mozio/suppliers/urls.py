# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy

from . import views

urlpatterns = [
    # URL pattern for the UserListView

    url(
        regex=r'^$',
        view=RedirectView.as_view(url=reverse_lazy('suppliers:service_area_create'), permanent=False),
        name='index'
    ),

    url(
        regex=r'^service-area/list/$',
        view=views.ServiceAreaListView.as_view(),
        name='service_area_list'
    ),

    url(
        regex=r'^service-area/add/$',
        view=views.ServiceAreaCreateView.as_view(),
        name='service_area_create'
    ),




]
