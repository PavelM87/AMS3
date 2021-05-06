from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Contract, Equipment, Operator, Report, Template

# admin.site.register(Report)
admin.site.register(Template)
# admin.site.register(Equipment)
admin.site.register(Operator)
admin.site.register(Contract)


@admin.register(Report)
class ReportAdmin(TranslationAdmin):
    pass


@admin.register(Equipment)
class EquipmentAdmin(TranslationAdmin):
    pass