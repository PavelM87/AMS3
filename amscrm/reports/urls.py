from django.urls import path
from reports import views


app_name = 'reports'

urlpatterns = [
    path('', views.ReportListView.as_view(), name='report-list'),
    # path('pdf/<int:pk>/', generate_pdf, name='pdf'),
    path('<int:pk>/', views.ReportDetailView.as_view(), name='report-detail'),
    path('create/', views.report_create, name='report-create'),
    path('<int:pk>/update/', views.report_update, name='report-update'),
    path('<int:pk>/delete/', views.ReportDeleteView.as_view(), name='report-delete'),
]