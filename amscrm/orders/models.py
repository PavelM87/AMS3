from datetime import date
from django.db import models

from objects.models import Object, Country, City, Region
from users.models import Team


class Order(models.Model):
    idOrder = models.AutoField(primary_key=True, unique=True)
    orderDate = models.DateField(default=date.today, verbose_name='Дата')
    orderCountry = models.ForeignKey(Country, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Страна')
    orderRegion = models.ForeignKey(Region, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Регион')
    orderCity = models.ForeignKey(City, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Город')
    orderAddress = models.CharField(max_length=100, verbose_name='Адрес')
    orderObject = models.ForeignKey(Object, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Объект')
    orderTeam = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Бригада')
    orderWorks = models.TextField(blank=True, verbose_name='Работы на объекте')
    orderContacts = models.TextField(blank=True, verbose_name='Контакты')
    orderCodes = models.TextField(blank=True, verbose_name='Коды работ')

    def __str__(self):
        return f"Наряд № {self.idOrder}"

    class Meta:
        verbose_name = "Наряд"
        verbose_name_plural = "Наряды"