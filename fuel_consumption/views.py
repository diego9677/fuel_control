from typing import Any
from datetime import timedelta
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, TemplateView
from django.utils import timezone
from django.db.models import Q, Prefetch

from .forms import FuelingForm, VehicleForm
from .models import Fueling, Vehicle


class DashboardTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        begin = timezone.now().replace(day=1, hour=0, minute=0, second=0)
        end = timezone.now().replace(day=1, month=begin.month + 1, hour=23, minute=59, second=59) - timedelta(days=1)

        # qs = Fueling.objects.filter(user=self.request.user, upload_date__range=(begin, end)).all()

        vehicles = Vehicle.objects.select_related('vehicle_type').prefetch_related(
            Prefetch('fuel_loads',
                     queryset=Fueling.objects.select_related('fuel_type').filter(upload_date__range=(begin, end)).order_by('-upload_date'))
        ).filter(user=self.request.user).all()

        liters = 0
        bills = 0

        for v in vehicles:
            loads = v.fuel_loads.all()
            for f in loads:
                bills += f.total
                liters += f.liters

        context['liters'] = round(liters)
        context['bills'] = round(bills)
        context['vehicles'] = vehicles

        # distance = (qs.last().odometer if qs.last() else 0) - (qs.first().odometer if qs.first() else 0)
        # context['distance'] = round(distance)
        # context['odometer'] = round(qs.last().odometer if qs.last() else 0)

        return context


class FuelingListView(LoginRequiredMixin, ListView):
    model = Fueling
    template_name = 'fuel_consumption/fueling_list.html'

    def get_queryset(self):
        search = self.request.GET.get('q', '')
        qs = Fueling.objects.select_related('fuel_type', 'vehicle', 'vehicle__vehicle_type').filter(
            Q(fuel_type__name__icontains=search),
            user=self.request.user
        ).order_by('-upload_date')[:20]
        return qs


class FuelingCreateView(LoginRequiredMixin, CreateView):
    model = Fueling
    form_class = FuelingForm
    success_url = reverse_lazy('fueling-list')
    template_name = 'fuel_consumption/fueling_form.html'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)


class FuelingUpdateView(LoginRequiredMixin, UpdateView):
    model = Fueling
    form_class = FuelingForm
    success_url = reverse_lazy('fueling-list')
    template_name = 'fuel_consumption/fueling_form.html'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)


class FuelingDeleteView(LoginRequiredMixin, DeleteView):
    model = Fueling
    success_url = reverse_lazy('fueling-list')
    template_name = 'fuel_consumption/fueling_confirm_delete.html'


class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'vehicle/vehicle_list.html'

    def get_queryset(self):
        search = self.request.GET.get('q', '')
        qs = Vehicle.objects.select_related('vehicle_type').filter(user=self.request.user, plate__icontains=search).all()
        return qs


class VehicleCreateView(LoginRequiredMixin, CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vehicle/vehicle_form.html'
    success_url = reverse_lazy('vehicle-list')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)


class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vehicle/vehicle_form.html'
    success_url = reverse_lazy('vehicle-list')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)


class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    model = Vehicle
    template_name = 'vehicle/vehicle_confirm_delete.html'
    success_url = reverse_lazy('vehicle-list')
