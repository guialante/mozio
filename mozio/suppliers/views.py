# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.views.generic import ListView, FormView
from django.core.urlresolvers import reverse_lazy

from braces.views import LoginRequiredMixin

from .forms import ServiceAreaForm
from .models import ServiceArea
from .viewmixins import LocationMixin


class ServiceAreaListView(LocationMixin, LoginRequiredMixin, ListView):
    """
        This view is used to load all service area associated to a user in the front end, and allow
        user to find a point in a bounded box in the service areas loaded.
    """
    template_name = 'suppliers/suppliers_list.html'
    queryset = ServiceArea.objects.all()

    def get_queryset(self):
        queryset = super(ServiceAreaListView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class ServiceAreaCreateView(LocationMixin, LoginRequiredMixin, FormView):
    """
        This view is used to create a service area, and show the last service area created.
    """
    form_class = ServiceAreaForm
    template_name = 'suppliers/suppliers_form.html'
    success_url = reverse_lazy('suppliers:service_area_create')

    def get_context_data(self, **kwargs):
        context = super(ServiceAreaCreateView, self).get_context_data(**kwargs)
        context['area'] = ServiceArea.objects.filter(user=self.request.user).last()
        return context

    def get_form_kwargs(self):
        kwargs = super(ServiceAreaCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        instance = form.save()
        self.get_context_data(instance=instance)
        return super(ServiceAreaCreateView, self).form_valid(form)
