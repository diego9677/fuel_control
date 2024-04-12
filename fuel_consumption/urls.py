from django.urls import path

from .views import FuelingListView, FuelingCreateView, FuelingUpdateView, FuelingDeleteView, DashboardTemplateView

urlpatterns = [
    path('dashboard/', DashboardTemplateView.as_view(), name='dashboard'),
    path('list/', FuelingListView.as_view(), name='fueling-list'),
    path('create/', FuelingCreateView.as_view(), name='fueling-create'),
    path('update/<int:pk>/', FuelingUpdateView.as_view(), name='fueling-update'),
    path('delete/<int:pk>/', FuelingDeleteView.as_view(), name='fueling-delete'),
]
