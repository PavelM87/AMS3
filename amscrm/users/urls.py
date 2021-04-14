from django.urls import path
from users import views


app_name = 'users'

urlpatterns = [
    path('', views.UserListView.as_view(), name='user-list'),
    path('team-list', views.TeamListView.as_view(), name='team-list'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('create/', views.UserCreateView.as_view(), name='user-create'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='user-update'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='user-delete'),
    path('team-create/', views.TeamCreateView.as_view(), name='team-create'),
    path('<int:pk>/change-password/', views.UserPasswordChangeView.as_view(), name='change-password'),
]
