from urllib.parse import urlparse
from django.urls import path, include
from orders.api import views

urlpatterns = [
    path('list/', views.OrderListView.as_view(), name='orders-list'),
    path('<int:pk>/create/', views.OrderCreateView.as_view(), name='orders-create'),
    path('<int:pk>/detail/', views.OrderDetailView.as_view(), name='order-detail'),
]
