from django.urls import path
from objects import views


app_name = 'objects'

urlpatterns = [
    path('', views.ObjectListView.as_view(), name='object-list'),
    path('<int:pk>/', views.ObjectDetailView.as_view(), name='object-detail'),
    path('create/', views.ObjectCreateView.as_view(), name='object-create'),
    path('<int:pk>/update/', views.ObjectUpdateView.as_view(), name='object-update'),
    path('<int:pk>/delete/', views.ObjectDeleteView.as_view(), name='object-delete'),
]