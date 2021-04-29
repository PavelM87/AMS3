from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect


class SuperuserAndLoginRequiredMixin(LoginRequiredMixin):
    """Verify that the current user is authenticated and is an organisor."""
    def dispatch(self, request, *args, **kwargs):
        print(request.user.userRole)
        if not request.user.is_authenticated or str(request.user.userRole) != 'Суперпользователь':
            return redirect("/")
        return super().dispatch(request, *args, **kwargs)


class ModeratorAndLoginRequiredMixin(LoginRequiredMixin):
    """Verify that the current user is authenticated and is an organisor."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or str(request.user.userRole) not in('Модератор', 'Суперпользователь'):
            return HttpResponse("Недостаточно прав доступа")
        return super().dispatch(request, *args, **kwargs)