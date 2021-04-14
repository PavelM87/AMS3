from django import forms
from .models import Report, Operator


class AMSEquipmentForm(forms.Form):
    type = forms.ChoiceField(choices=(
            ('panel_antenna', 'панельная антенна'),
            ('RRL_antenna', 'РРЛ антенна'),
            ('radio_module', 'радиомодуль'),
        ), label='Тип')
    height = forms.IntegerField(label='Высота')
    proportions = forms.IntegerField(label='Размеры')
    amount = forms.IntegerField(label='Количество')
    manufacturer = forms.CharField(max_length=50, label='Производитель')
    model = forms.CharField(max_length=50, label='Модель')
    operator = forms.ModelChoiceField(queryset=Operator.objects.all(), label='Оператор')
    note = forms.CharField(max_length=100, label='Примечание')


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


