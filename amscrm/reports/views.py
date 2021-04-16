# import tempfile
import json

from django.core.exceptions import ObjectDoesNotExist
from django.forms import formset_factory
# from django.template.loader import render_to_string
from django.http import HttpResponse
# from django.template.loader import get_template
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views import generic

# from amscrm import settings
from .forms import AMSEquipmentForm, ReportModelForm
from .models import Equipment, Operator, Report

# from weasyprint import HTML, CSS
# from users.mixins import SuperuserAndLoginRequiredMixin, ModeratorAndLoginRequiredMixin



# def my_view(request):
#     EquipmentFormset = formset_factory(AMSEquipmentForm)
#     formset = EquipmentFormset
#     context = {}
#     if request.method == 'POST':
#         form = AMSEquipmentForm(request.POST)
#         if form.is_valid():
#             context['type'] = form.cleaned_data['type']
#             context['height'] = form.cleaned_data['height']
#             context['proportions'] = form.cleaned_data['proportions']
#             context['amount'] = form.cleaned_data['amount']
#             context['manufacturer'] = form.cleaned_data['manufacturer']
#             context['model'] = form.cleaned_data['model']
#             context['operator'] = form.cleaned_data['operator']
#             context['note'] = form.cleaned_data['note']
#             print(context)
#             context = json.dumps(context)
#             print(context)

#             return redirect("reports:report-list")
#     else:
#         form = AMSEquipmentForm()
#     return render(request, "reports/amsequip.html", {'form': form})


class OperatorEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Operator):
            return obj.operatorName
        return json.JSONEncoder.default(self, obj)


def report_create(request):
    context = {}
    EquipmentFormset = formset_factory(AMSEquipmentForm)
    form = ReportModelForm(request.POST or None)
    formset = EquipmentFormset(request.POST or None, prefix='reports_report')
    if request.method == "POST":
        # print(f"FORMSET: {formset.is_valid()} errors: {formset.errors}")
        # print(f"FORM: {form.is_valid()} errors: {form.errors}")
        if form.is_valid() and formset.is_valid():
            data = form.save(commit=False)
            data.reportEquipAms = json.dumps(formset.cleaned_data, cls=OperatorEncoder)
            data.save()
            return redirect("reports:report-list")
    context['formset'] = formset
    context['form'] = form
    return render(request, 'reports/report_create.html', context)


def report_update(request, pk):
    EquipmentFormset = formset_factory(AMSEquipmentForm, max_num=1) # max_num=1 запрещает пустые поля при редактировании
    report = Report.objects.get(idReport=pk)
    # equipment = Equipment.objects.filter(idEquipment=report.reportEquipment_id)
    form = ReportModelForm(instance=report)
    formset = EquipmentFormset(initial=json.loads(report.reportEquipAms), prefix='reports_report')
    if request.method == 'POST':
        form = ReportModelForm(request.POST or None)
        formset = EquipmentFormset(request.POST or None, prefix='reports_report')
        print(f"FORMSET: {formset.is_valid()} errors: {formset.errors}")
        print(f"FORM: {form.is_valid()} errors: {form.errors}")
        if form.is_valid() and formset.is_valid():
            report.reportYear = form.cleaned_data['reportYear']
            report.reportObject_id = form.cleaned_data['reportObject']
            report.reportTemplate_id = form.cleaned_data['reportTemplate']
            report.reportTeam_id = form.cleaned_data['reportTeam']
            report.reportEquipment_id = form.cleaned_data['reportEquipment']
            report.reportWind = form.cleaned_data['reportWind']
            report.reportWeather = form.cleaned_data['reportWeather']
            report.reportSoil = form.cleaned_data['reportSoil']
            report.reportTemp = form.cleaned_data['reportTemp']
            report.reportWeather3 = form.cleaned_data['reportWeather3']
            report.reportElVoltage = form.cleaned_data['reportElVoltage']
            report.reportElCableL = form.cleaned_data['reportElCableL']
            report.reportElCableR = form.cleaned_data['reportElCableR']
            report.reportElRope = form.cleaned_data['reportElRope']
            report.reportElBus = form.cleaned_data['reportElBus']
            report.reportMeasuresDate = form.cleaned_data['reportMeasuresDate']
            report.reportData = form.cleaned_data['reportData']
            # print()
            # print(formset.cleaned_data)
            # print()
            # print(report.__dict__)
            # print()
            # print(form.cleaned_data)
            # # print(report.reportEquipAms)
            report.reportEquipAms = json.dumps(formset.cleaned_data, cls=OperatorEncoder, ensure_ascii=False)
            report.save()
            return redirect('reports:report-list')
    context = {
        'report': report,
        'form': form,
        'formset': formset
    }
    return render(request, "reports/report_update.html", context)


# def ams_equip(request):
#     report = Report.objects.all()
#     context = {}
#     if request.method == 'POST':
#         form = AMSEquipmentForm(request.POST)
#         if form.is_valid():
#             context['type'] = form.cleaned_data['type']
#             context['height'] = form.cleaned_data['height']
#             context['proportions'] = form.cleaned_data['proportions']
#             context['amount'] = form.cleaned_data['amount']
#             context['manufacturer'] = form.cleaned_data['manufacturer']
#             context['model'] = form.cleaned_data['model']
#             context['operator'] = form.cleaned_data['operator']
#             context['note'] = form.cleaned_data['note']
#             print(context)
#             context = json.dumps(context)
#             print(context)

#             return redirect("reports:report-list")
#     else:
#         form = AMSEquipmentForm()
#     return render(request, "reports/amsequip.html", {'form': form})




def generate_pdf(request, *args, **kwargs):
    """Создание pdf."""
    # Данные модели
    pk = kwargs.get('pk')
    report = get_object_or_404(Report, pk=pk)

    # Обработка шаблона
    html_string = render_to_string('reports/pdf.html', {'report': report})
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf()

    # Создание http ответа
    pdf = html.write_pdf(stylesheets=[CSS(settings.STATIC_ROOT + '/css/pdf_report.css')])
    response = HttpResponse(pdf, content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=report.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
    return response


class ReportListView(generic.ListView):
    template_name = "reports/report_list.html"
    queryset = Report.objects.all()
    context_object_name = "reports"


class ReportDetailView(generic.DetailView):
    template_name = "reports/report_detail.html"
    queryset = Report.objects.all()
    context_object_name = "report"

    def get_context_data(self, **kwargs):
        context = super(ReportDetailView, self).get_context_data(**kwargs)
        try:
            context['equipment'] = Equipment.objects.filter(idEquipment=kwargs['object'].reportEquipment_id)
        except ObjectDoesNotExist:
            context['equipment'] = 'Отсутствует'
        context['ams_equip'] = json.loads(context['object'].reportEquipAms)
        print(context)
        return context


class ReportCreateView(generic.CreateView):
    template_name = "reports/report_create.html"
    form_class = ReportModelForm

    def get_success_url(self):
        return reverse("reports:report-list")


class ReportUpdateView(generic.UpdateView):
    template_name = "reports/report_update.html"
    queryset = Report.objects.all()
    form_class = ReportModelForm

    def get_success_url(self):
        return reverse("reports:report-list")


class ReportDeleteView(generic.DeleteView):
    template_name = "reports/report_delete.html"
    queryset = Report.objects.all()

    def get_success_url(self):
        return reverse("reports:report-list")





