from datetime import date
from django.db import models
from django.core.serializers.json import DjangoJSONEncoder

from users.models import Team
from objects.models import Object


class Report(models.Model):
	idReport = models.AutoField(primary_key=True, unique=True)
	reportYear = models.CharField(max_length=45)
	reportObject = models.ForeignKey(Object, null=True, on_delete=models.SET_NULL)
	reportTemplate = models.ForeignKey("Template", null=True, on_delete=models.SET_NULL)
	reportData = models.JSONField()
	reportTeam = models.ForeignKey(Team, on_delete=models.PROTECT)
	reportEquipment = models.ForeignKey("Equipment", null=True, on_delete=models.SET_NULL)
	reportWind = models.CharField(max_length=45)
	reportWeather = models.CharField(max_length=45)
	reportSoil = models.CharField(max_length=45)
	reportTemp = models.CharField(max_length=45)
	reportWeather3 = models.CharField(max_length=45)
	reportElVoltage = models.CharField(max_length=45)
	reportElCableL = models.CharField(max_length=45)
	reportElCableR = models.CharField(max_length=45)
	reportElRope = models.CharField(max_length=45)
	reportElBus = models.CharField(max_length=45)
	reportEquipAms = models.JSONField(encoder=DjangoJSONEncoder, null=True)
	reportPhotosRes = models.JSONField(null=True)
	reportPDataAms = models.JSONField(null=True)
	reportDate = models.DateField(auto_now_add=True)
	reportMeasuresDate = models.DateField(default=date.today)

	def __str__(self):
		return f"Отчет № {self.idReport}"

	class Meta:

		constraints = [
			models.UniqueConstraint(fields=['idReport', 'reportEquipment'], name='unique_equipment')
		]
		verbose_name = "Отчет"
		verbose_name_plural = "Отчеты"
		db_table = "reports_report"


class Template(models.Model):
	idTemplate = models.AutoField(primary_key=True, unique=True)
	templateName = models.CharField(max_length=45)
	templatePath = models.CharField(max_length=255)

	def __str__(self):
		return self.templateName

	class Meta:
		verbose_name = "Шаблон"
		verbose_name_plural = "Шаблоны"


class Equipment(models.Model):
	idEquipment = models.AutoField(primary_key=True, unique=True)
	equipName = models.CharField(max_length=255)
	equipNum = models.CharField(max_length=255)
	equipRange = models.CharField(max_length=255)
	equipError = models.CharField(max_length=255)
	equipDateCur = models.DateField()
	equipDateNext = models.DateField()
	equipDocNum = models.CharField(max_length=45)

	def __str__(self):
		return self.equipName

	class Meta:
		verbose_name = "Инструмент"
		verbose_name_plural = "Инструменты"
		db_table = 'reports_equipment'


class Operator(models.Model):
	idOperator = models.AutoField(primary_key=True)
	operatorName = models.CharField(max_length=45)
	operatorReport = models.ForeignKey("Report", null=True, on_delete=models.SET_NULL)
	operatorContract = models.ForeignKey("Contract",null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.operatorName

	class Meta:
		verbose_name = "Оператор"
		verbose_name_plural = "Операторы"


class Contract(models.Model):
	idContract = models.AutoField(primary_key=True, unique=True)
	contractName = models.CharField(max_length=45)
	limits = models.JSONField(null=True)

	def __str__(self):
		return self.contractName

	class Meta:
		verbose_name = "Контракт"
		verbose_name_plural = "Контракты"


class JSON(models.Model):
    file_name = models.CharField(max_length=120, null=True)
    json_file = models.FileField(upload_to='jsons', null=True)
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)   
    
    def __str__(self):
        return  str(self.file_name)




















