from django.urls import path
from orders import views


app_name = 'orders'

urlpatterns = [
    path('', views.OrderListView.as_view(), name='order-list'),
    path('<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('create/', views.OrderCreateView.as_view(), name='order-create'),
    path('<int:pk>/update/', views.OrderUpdateView.as_view(), name='order-update'),
    path('<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order-delete'),
]