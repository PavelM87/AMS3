import django_filters
from django_filters import CharFilter, BooleanFilter

from .models import Order


class OrderAddressFilter(django_filters.FilterSet):
    orderAddress = CharFilter(lookup_expr='icontains', label='Адрес')
    in_work = BooleanFilter(field_name='orderTeam', lookup_expr='isnull',exclude=True, label='В работе')
    

    class Meta:
        model = Order
        fields = ['orderCountry', 'orderRegion', 'orderCity', 'orderTeam']