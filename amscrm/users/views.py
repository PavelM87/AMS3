from django.shortcuts import render, reverse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse_lazy
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.core import exceptions

from .models import CustomUser, Team
from .forms import UserModelForm, CustomUserCreationForm, CustomUserChangeForm, TeamModelForm
from .mixins import SuperuserAndLoginRequiredMixin


class LandingPageView(generic.View):

    def get(self, request):
        user = CustomUser.objects.all()
        context = {
            'user': user,
        }
        return render(request, 'landing.html', context)	


class UserPasswordChangeView(SuperuserAndLoginRequiredMixin, views.PasswordChangeView):
    success_url = reverse_lazy('password_change_done')
    pk = []

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.pk.append(kwargs['pk'])
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self, pk=pk):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = CustomUser.objects.get(idUser=pk.pop())
        return kwargs


class UserPasswordChangeDoneView(SuperuserAndLoginRequiredMixin, views.PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'


class UserListView(SuperuserAndLoginRequiredMixin, generic.ListView):
    template_name = "users/user_list.html"
    queryset = CustomUser.objects.all()
    context_object_name = "users"	


class UserDetailView(SuperuserAndLoginRequiredMixin, generic.DetailView):
    template_name = "users/user_detail.html"
    queryset = CustomUser.objects.all()
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        try:
            context['team'] = Team.objects.get(member=kwargs['object'].idUser)
        except exceptions.ObjectDoesNotExist:
            context['team'] = '???? ??????????????'
        return context


class UserCreateView(SuperuserAndLoginRequiredMixin, generic.CreateView):
    template_name = "users/user_create.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("users:user-list")


class UserUpdateView(SuperuserAndLoginRequiredMixin, generic.UpdateView):
    template_name = "users/user_update.html"
    queryset = CustomUser.objects.all()
    form_class = UserModelForm
    context_object_name = "user"

    def get_success_url(self):
        return reverse("users:user-list")


class UserDeleteView(generic.DeleteView):
    template_name = "users/user_delete.html"
    queryset = CustomUser.objects.all()

    def get_success_url(self):
        return reverse("users:user-list")


class TeamListView(SuperuserAndLoginRequiredMixin, generic.ListView):
    template_name = "users/team_list.html"
    queryset = Team.objects.all()
    context_object_name = "teams" 


class TeamCreateView(SuperuserAndLoginRequiredMixin, generic.CreateView):
    template_name = "users/team_create.html"
    form_class = TeamModelForm

    def get_success_url(self):
        return reverse("users:user-list")

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        return super().post(request, *args, **kwargs)
