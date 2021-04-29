from django.shortcuts import render, reverse
from django.views import generic

from .models import Object
from .forms import ObjectModelForm
from users.mixins import ModeratorAndLoginRequiredMixin


class ObjectListView(ModeratorAndLoginRequiredMixin, generic.ListView):
    template_name = "objects/object_list.html"
    queryset = Object.objects.all()
    context_object_name = "objects"


class ObjectDetailView(ModeratorAndLoginRequiredMixin, generic.DetailView):
    template_name = "objects/object_detail.html"
    queryset = Object.objects.all()
    context_object_name = "object"


class ObjectUpdateView(ModeratorAndLoginRequiredMixin, generic.UpdateView):
    template_name = "objects/object_update.html"
    queryset = Object.objects.all()
    form_class = ObjectModelForm

    def get_success_url(self):
        return reverse("objects:object-list")


class ObjectCreateView(ModeratorAndLoginRequiredMixin, generic.CreateView):
    template_name = "objects/object_create.html"
    form_class = ObjectModelForm

    def get_success_url(self):
        return reverse("objects:object-list")


class ObjectDeleteView(ModeratorAndLoginRequiredMixin, generic.DeleteView):
    template_name = "objects/object_delete.html"
    queryset = Object.objects.all()

    def get_success_url(self):
        return reverse("objects:object-list")