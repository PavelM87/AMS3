from django import forms

from .models import Report, Operator


class AMSEquipmentForm(forms.Form):
    EQ_TYPES = (
        ('panel_antenna', 'панельная антенна'),
        ('RRL_antenna', 'РРЛ антенна'),
        ('radio_module', 'радиомодуль')
    )
    eq_type = forms.ChoiceField(choices=EQ_TYPES, label='Тип')
    height = forms.IntegerField(label='Высота')
    proportions = forms.IntegerField(label='Размеры')
    amount = forms.IntegerField(label='Количество')
    manufacturer = forms.CharField(max_length=50, label='Производитель')
    model = forms.CharField(max_length=50, label='Модель')
    operator = forms.ModelChoiceField(queryset=Operator.objects.all(), label='Оператор', empty_label=None)
    note = forms.CharField(max_length=100, label='Примечание')

    eq_type.widget.attrs.update({'class': 'formset-field'})
    height.widget.attrs.update({'class': 'formset-field'})
    proportions.widget.attrs.update({'class': 'formset-field'})
    amount.widget.attrs.update({'class': 'formset-field'})
    manufacturer.widget.attrs.update({'class': 'formset-field'})
    model.widget.attrs.update({'class': 'formset-field'})
    operator.widget.attrs.update({'class': 'formset-field'})
    note.widget.attrs.update({'class': 'formset-field'})



class ReportModelForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            'reportYear',
            'reportObject',
            'reportTemplate',
            'reportData',
            'reportTeam',
            'reportEquipment',
            'reportWind',
            'reportWeather',
            'reportSoil',
            'reportTemp',
            'reportWeather3',
            'reportElVoltage',
            'reportElCableL',
            'reportElCableR',
            'reportElRope',
            'reportElBus',
            'reportMeasuresDate',
        ]

        labels = {
            'reportYear': 'Год',
            'reportObject': 'Объект',
            'reportTemplate': 'Шаблон',
            'reportData': 'Данные',
            'reportTeam': 'Бригада',
            'reportEquipment': 'Инструменты измерений',
            'reportWind': 'Ветер',
            'reportWeather': 'Погода в день измерени',
            'reportSoil': 'Грунт',
            'reportTemp': 'Температура',
            'reportWeather3': 'Погода в последние 3 дня',
            'reportElVoltage': 'Питающее напряжение СОМ',
            'reportElCableL': 'Марка кабеля СОМ (тип слева)',
            'reportElCableR': 'Марка кабеля СОМ (сечение справа)',
            'reportElRope': 'Молниеприемник – трос молниеприемника',
            'reportElBus': 'Шина (проводник) контура заземления',
            'reportMeasuresDate': 'Дата произведения измерений'
        }


