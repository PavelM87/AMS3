from django import forms

from .models import Report, Operator


class ResultDataForm(forms.Form):
    distance = forms.IntegerField(min_value=0,label='Pасстояние')
    height_1 = forms.IntegerField(min_value=0,)
    height_2 = forms.IntegerField(min_value=0,)
    height_3 = forms.IntegerField(min_value=0,)
    height_4 = forms.IntegerField(min_value=0,)
    height_5 = forms.IntegerField(min_value=0,)
    c_left_1_0 = forms.DecimalField(min_value=0, max_digits=7, decimal_places=1)
    c_left_1_1 = forms.DecimalField(min_value=0,max_digits=7, decimal_places=1)
    c_left_2_0 = forms.DecimalField(min_value=0,max_digits=7, decimal_places=1)
    c_left_2_1 = forms.DecimalField(min_value=0,max_digits=7, decimal_places=1)
    c_left_3_0 = forms.DecimalField(min_value=0,max_digits=7, decimal_places=1)
    c_left_3_1 = forms.DecimalField(min_value=0,max_digits=7, decimal_places=1)
    c_left_4_0 = forms.DecimalField(min_value=0,max_digits=7, decimal_places=1)
    c_left_4_1 = forms.DecimalField(min_value=0,max_digits=7, decimal_places=1)
    c_left_5_0 = forms.DecimalField(min_value=0,max_digits=7, decimal_places=1)
    c_left_5_1 = forms.DecimalField(min_value=0,max_digits=7, decimal_places=1)
    c_right_1_0 = forms.DecimalField(min_value=0,max_digits=7, decimal_places=3)
    c_right_1_1 = forms.DecimalField(min_value=0,max_digits=7, decimal_places=3)
    c_right_2_0 = forms.DecimalField(min_value=0,max_digits=7, decimal_places=3)
    c_right_2_1 = forms.DecimalField(min_value=0,max_digits=7, decimal_places=3)
    c_right_3_0 = forms.DecimalField(min_value=0,max_digits=7, decimal_places=3)
    c_right_3_1 = forms.DecimalField(min_value=0,max_digits=7, decimal_places=3)
    c_right_4_0 = forms.DecimalField(min_value=0,max_digits=7, decimal_places=3)
    c_right_4_1 = forms.DecimalField(min_value=0,max_digits=7, decimal_places=3)
    c_right_5_0 = forms.DecimalField(min_value=0,max_digits=7, decimal_places=3)
    c_right_5_1 = forms.DecimalField(min_value=0,max_digits=7, decimal_places=3)


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


