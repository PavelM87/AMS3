from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from users.views import LandingPageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('objects/', include('objects.urls', namespace='objects')),
    path('reports/', include('reports.urls', namespace='reports')),
    path('users/', include('users.urls', namespace='users')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change_done', PasswordChangeDoneView.as_view(), name='password_change_done'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
