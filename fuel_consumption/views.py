from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from .forms import FuelingForm
from .models import Fueling


class FuelingListView(LoginRequiredMixin, ListView):
    model = Fueling
    template_name = 'fuel_consumption/fueling_list.html'

    def get_queryset(self):
        qs = Fueling.objects.filter(user=self.request.user).order_by('-upload_date')[:20]
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
