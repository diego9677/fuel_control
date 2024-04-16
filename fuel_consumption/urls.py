from django.urls import path

from .views import (
    FuelingListView,
    FuelingCreateView,
    FuelingUpdateView,
    FuelingDeleteView,
    DashboardTemplateView,
    VehicleListView,
    VehicleCreateView,
    VehicleUpdateView,
    VehicleDeleteView,
)

urlpatterns = [
    path('dashboard/', DashboardTemplateView.as_view(), name='dashboard'),
    path('list/', FuelingListView.as_view(), name='fueling-list'),
    path('create/', FuelingCreateView.as_view(), name='fueling-create'),
    path('update/<int:pk>/', FuelingUpdateView.as_view(), name='fueling-update'),
    path('delete/<int:pk>/', FuelingDeleteView.as_view(), name='fueling-delete'),
    path('vehicle/list/', VehicleListView.as_view(), name='vehicle-list'),
    path('vehicle/create/', VehicleCreateView.as_view(), name='vehicle-create'),
    path('vehicle/update/<int:pk>/', VehicleUpdateView.as_view(), name='vehicle-update'),
    path('vehicle/delete/<int:pk>/', VehicleDeleteView.as_view(), name='vehicle-delete'),
]
