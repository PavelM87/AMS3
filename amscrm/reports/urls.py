from django.urls import path
from reports import views


app_name = 'reports'

urlpatterns = [
    path('', views.ReportListView.as_view(), name='report-list'),
    # path('pdf/<int:pk>/', generate_pdf, name='pdf'),
    path('<int:pk>/', views.ReportDetailView.as_view(), name='report-detail'),
    path('create/', views.ReportCreateView.as_view(), name='report-create'),
    path('<int:pk>/update/', views.ReportUpdateView.as_view(), name='report-update'),
    path('<int:pk>/delete/', views.ReportDeleteView.as_view(), name='report-delete'),
    path('amsequip', views.create, name='amsequip'),
]