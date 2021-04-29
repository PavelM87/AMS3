from django.shortcuts import render, reverse
from django.views import generic

from .forms import OrderModelForm
from .models import Order
from .filters import OrderAddressFilter
from users.mixins import SuperuserAndLoginRequiredMixin, ModeratorAndLoginRequiredMixin


class OrderListView(SuperuserAndLoginRequiredMixin, generic.ListView):
    template_name = "orders/order_list.html"
    queryset = Order.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = OrderAddressFilter(self.request.GET, queryset=self.get_queryset())
        return context


class OrderDetailView(SuperuserAndLoginRequiredMixin, generic.DetailView):
    template_name = "orders/order_detail.html"
    queryset = Order.objects.all()
    context_object_name = "order"


class OrderCreateView(SuperuserAndLoginRequiredMixin, generic.CreateView):
    template_name = "orders/order_create.html"
    form_class = OrderModelForm

    def get_success_url(self):
        return reverse("orders:order-list")


class OrderUpdateView(SuperuserAndLoginRequiredMixin, generic.UpdateView):
    template_name = "orders/order_update.html"
    queryset = Order.objects.all()
    form_class = OrderModelForm

    def get_success_url(self):
        return reverse("orders:order-list")


class OrderDeleteView(SuperuserAndLoginRequiredMixin, generic.DeleteView):
    template_name = "orders/order_delete.html"
    queryset = Order.objects.all()

    def get_success_url(self):
        return reverse("orders:order-list")
