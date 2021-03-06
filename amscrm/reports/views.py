import tempfile
import json
import simplejson

from django.core.exceptions import ObjectDoesNotExist
from django.forms import formset_factory
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views import generic

from amscrm import settings
from .forms import AMSEquipmentForm, ReportModelForm, ResultDataForm
from .models import Equipment, Operator, Report, JSON, Template
from users.models import Team
from objects.models import Object

from weasyprint import HTML, CSS
# from users.mixins import SuperuserAndLoginRequiredMixin, ModeratorAndLoginRequiredMixin


class OperatorEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Operator):
            return obj.idOperator
        return json.JSONEncoder.default(self, obj)
        


def json_upload_view(request):
    if request.method == 'POST':
        
        json_file_name = request.FILES.get('file').name
        json_file = request.FILES.get('file')
        obj, created = JSON.objects.get_or_create(file_name=json_file_name)

        if created:
            obj.json_file = json_file
            obj.save()
            with open(obj.json_file.path, 'r') as f:
                data = json.load(f)
                form = data['reportEquipAms']
                for dct in form:
                    dct['operator'] = Operator.objects.get(operatorName=dct['operator']).idOperator
                report_obj = Report.objects.create(
                    reportYear=data['reportYear'],
                    reportObject=Object.objects.get(objNum=data['reportObject'].split()[1]),
                    reportTemplate=Template.objects.get(templateName=data['reportTemplate']),
                    reportData=data['reportData'],
                    reportTeam=Team.objects.get(id=data['reportTeam'].split()[-1]),
                    reportEquipment=Equipment.objects.get(equipName=data['reportEquipment']),
                    reportWind=data['reportWind'],
                    reportTemp=data['reportTemp'],
                    reportWeather=data['reportWeather'],
                    reportSoil=data['reportSoil'],
                    reportWeather3=data['reportWeather3'],
                    reportElVoltage=data['reportElVoltage'],
                    reportElCableL=data['reportElCableL'],
                    reportElCableR=data['reportElCableR'],
                    reportElRope=data['reportElRope'],
                    reportElBus=data['reportElBus'],
                    reportEquipAms=json.dumps(form, cls=OperatorEncoder),
                    reportPhotosRes=data['reportPhotosRes'],
                    reportPDataAms=data['reportPDataAms'],
                    reportDate=data['reportDate']
                )
                report_obj.save()
                return JsonResponse({'ex': False})
        else:
            return JsonResponse({'ex': True})

    return HttpResponse()


def report_create(request):
    context = {}
    EquipmentFormset = formset_factory(AMSEquipmentForm, extra=1)
    ResultDataFormset = formset_factory(ResultDataForm, extra=2)
    form = ReportModelForm(request.POST or None)
    formset = EquipmentFormset(request.POST or None, prefix='reports_report')
    formset_res = ResultDataFormset(request.POST or None)
    if request.method == "POST":
        print(f"FORMSET: {formset.is_valid()} errors: {formset.errors}")
        print(f"FORMSET_RES: {formset_res.is_valid()} errors: {formset_res.errors}")
        print(f"FORM: {form.is_valid()} errors: {form.errors}")
        # print(formset_res.cleaned_data)
        if form.is_valid() and formset.is_valid() and formset_res.is_valid():
            data = form.save(commit=False)
            data.reportEquipAms = json.dumps(formset.cleaned_data, cls=OperatorEncoder)
            data.reportData = simplejson.dumps(formset_res.cleaned_data)
            data.save()
            return redirect("reports:report-list")
        
    context['formset'] = formset
    context['formset_res'] = formset_res
    context['form'] = form
    # print(context['formset_res'])
    return render(request, 'reports/report_create.html', context)


def report_update(request, pk):
    EquipmentFormset = formset_factory(AMSEquipmentForm, max_num=1) # max_num=1 ?????????????????? ???????????? ???????? ?????? ????????????????????????????
    ResultDataFormset = formset_factory(ResultDataForm, max_num=1) 
    report = Report.objects.get(idReport=pk)
    form = ReportModelForm(instance=report)
    formset = EquipmentFormset(initial=json.loads(report.reportEquipAms), prefix='reports_report')
    formset_res = ResultDataFormset(initial=json.loads(report.reportData))
    if request.method == 'POST':
        form = ReportModelForm(request.POST or None)
        formset = EquipmentFormset(request.POST or None, prefix='reports_report')
        formset_res = ResultDataFormset(request.POST or None,)
        print(f"FORMSET: {formset.is_valid()} errors: {formset.errors}")
        print(f"FORMSET_RES: {formset_res.is_valid()} errors: {formset_res.errors}")
        print(f"FORM: {form.is_valid()} errors: {form.errors}")
        if form.is_valid() and formset.is_valid() and formset_res.is_valid():
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
            report.reportData = simplejson.dumps(formset_res.cleaned_data)
            report.reportEquipAms = json.dumps(formset.cleaned_data, cls=OperatorEncoder, ensure_ascii=False)
            report.save()
            return redirect('reports:report-list')
    context = {
        'report': report,
        'form': form,
        'formset': formset,
        'formset_res': formset_res
    }
    return render(request, "reports/report_update.html", context)


def generate_pdf(request, *args, **kwargs):
    """???????????????? pdf."""
    # ???????????? ????????????
    pk = kwargs.get('pk')
    report = get_object_or_404(Report, pk=pk)
    equipment = Equipment.objects.filter(idEquipment=report.reportEquipment_id)
    ams_equip = json.loads(report.reportEquipAms)
    context = {
        'report': report,
        'equipment': equipment,
        'ams_equip': ams_equip
    }
    return render(request, "reports/pdf.html", context)

    # # ?????????????????? ??????????????
    # html_string = render_to_string('reports/pdf.html', {'report': report, 'equipment': equipment, 'ams_equip': ams_equip})
    # html = HTML(string=html_string, base_url=request.build_absolute_uri())
    # result = html.write_pdf()

    # # ???????????????? http ????????????
    # pdf = html.write_pdf()
    # response = HttpResponse(pdf, content_type='application/pdf;')
    # response['Content-Disposition'] = 'inline; filename=report.pdf'
    # response['Content-Transfer-Encoding'] = 'binary'
    # with tempfile.NamedTemporaryFile(delete=True) as output:
    #     output.write(result)
    #     output.flush()
    #     output = open(output.name, 'rb')
    #     response.write(output.read())
    # return response

class UploadTemplateView(generic.TemplateView):
    template_name = 'reports/json_from_file.html'


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
            context['equipment'] = '??????????????????????'
        data_ams_equip = json.loads(context['object'].reportEquipAms)
        for form in data_ams_equip:
            form['operator'] = Operator.objects.get(idOperator=form['operator'])
        context['ams_equip'] = data_ams_equip
        context['result_data'] = json.loads(context['object'].reportData)
        context['operator'] = Operator.objects.all()
        return context


# class ReportCreateView(generic.CreateView):
#     template_name = "reports/report_create.html"
#     form_class = ReportModelForm

#     def get_success_url(self):
#         return reverse("reports:report-list")


# class ReportUpdateView(generic.UpdateView):
#     template_name = "reports/report_update.html"
#     queryset = Report.objects.all()
#     form_class = ReportModelForm

#     def get_success_url(self):
#         return reverse("reports:report-list")


class ReportDeleteView(generic.DeleteView):
    template_name = "reports/report_delete.html"
    queryset = Report.objects.all()

    def get_success_url(self):
        return reverse("reports:report-list")





