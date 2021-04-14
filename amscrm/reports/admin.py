from django.contrib import admin

from .models import Report, Template, Equipment, Operator, Contract


admin.site.register(Report)
admin.site.register(Template)
admin.site.register(Equipment)
admin.site.register(Operator)
admin.site.register(Contract)