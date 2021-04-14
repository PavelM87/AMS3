# import tempfile
import json
# from weasyprint import HTML, CSS

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction, IntegrityError
# from django.template.loader import render_to_string
from django.http import HttpResponse
# from django.template.loader import get_template
from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views import generic
from django.forms import modelformset_factory, formset_factory

# from amscrm import settings
from .forms import ReportModelForm, AMSEquipmentForm
from .models import Report, Equipment, Operator
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


def create(request):
    context = {}
    EquipmentFormset = formset_factory(AMSEquipmentForm, extra=1)
    form = ReportModelForm(request.POST or None)
    formset = EquipmentFormset(request.POST or None, prefix='reports_report')
    if request.method == "POST":
        print(f'formset {formset.is_valid()}||form{form.is_valid()}')
        print(f'formset {formset.errors}||form{form.errors}')
        if form.is_valid() and formset.is_valid():
            data = form.save(commit=False)
            data.reportEquipAms = json.dumps(formset.cleaned_data, cls=OperatorEncoder)
            data.save()
            return redirect("reports:report-list")
    context['formset'] = formset
    context['form'] = form
    return render(request, 'reports/amsequip.html', context)


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
        return context


class ReportCreateView(generic.CreateView):
    template_name = "reports/report_create.html"
    form_class = ReportModelForm

    def get_success_url(self):
        return reverse("reports:report-list")


# def report_update(request, pk):

#     report = Report.objects.get(id=pk)
#     form = ReportModelForm(instance=report)
#     equipment = AMSEquipment.objects.filter(ams_id=report.ams_id)
#     # formset = AMSEquipmentForm(instance=equipment)
#     if request.method == 'POST':
#         form = ReportModelForm(request.POST, instance=report)
#         if form.is_valid():
#             form.save()
#             return redirect('/reports')
#     context = {
#         'report': report,
#         'form': form
#     }
#     return render(request, "reports/report_update.html", context)




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





