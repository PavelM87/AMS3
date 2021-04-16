from django.db import models
from django.utils import timezone


class Object(models.Model):
	AMS_TYPES = (
		('square', 'Квадрат'),
		('triangle', 'Треугольник'),
		('circle', 'Круг')
	)
	AMS_SECTIONS = (
		('tower', 'Башня'),
		('mast', 'Мачта'),
		('roof_mast', 'Мачта на кровле'),
		('pillar', 'Столб'),
		('tripod', 'Трипод'),
		('roof_monopole', 'Монополь (на кровле)')
	)
	FERM_TYPE = (
		('sq_ferm', 'ферма квадратная'),
		('tr_ferm', 'ферма треугольная'),
		('pipe', 'труба'),
		('pillar', 'столб')
	)
	idObject = models.AutoField(primary_key=True)
	objReg = models.CharField(max_length=5, null=True, blank=True)
	objNum = models.IntegerField(null=True, blank=True)
	objGeoLat = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
	objGeoLng = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
	objCountry = models.ForeignKey("Country", null=True, on_delete=models.SET_NULL)
	objRegion = models.ForeignKey("Region", null=True, on_delete=models.SET_NULL)
	objCity = models.ForeignKey("City", null=True, on_delete=models.SET_NULL)
	objStatus = models.BooleanField(default=True)
	objNote = models.TextField()
	objAddress = models.CharField(max_length=255, null=True, blank=True)
	objAmsType = models.CharField(choices=AMS_TYPES, max_length=8, default='Квадрат')
	objAmsSection = models.CharField(choices=AMS_SECTIONS, max_length=15, default='Квадрат')
	objFermType = models.CharField(choices=FERM_TYPE, max_length=7, default='ферма квадратная')
	sectionLength = models.IntegerField()
	amsHeight = models.IntegerField()
	signalSigns = models.BooleanField(default=True)
	amsDeviation = models.DecimalField(max_digits=5, decimal_places=2)
	amsFastenHeight = models.DecimalField(max_digits=4, decimal_places=2)
	amsRopeDia = models.DecimalField(max_digits=5, decimal_places=2)
	amsRopesQty = models.IntegerField()
	amsTension = models.DecimalField(max_digits=5, decimal_places=2)
	amsWaterproof = models.TextField(null=True, blank=True)
	amsProducer = models.CharField(max_length=255, null=True, blank=True)
	amsOperator = models.CharField(max_length=255, null=True, blank=True)
	amsDocsDev = models.CharField(max_length=255, null=True, blank=True)
	amsImgPlan = models.ImageField(null=True, blank=True)
	amsImgEquip = models.ImageField(null=True, blank=True)
	amsImgPhotos = models.ImageField(null=True, blank=True)
	objDate = models.DateTimeField(default=timezone.now, null=True, blank=True)
	tblObjectscol = models.CharField(max_length=45, null=True, blank=True)

	def __str__(self):
		return f"{self.objReg} {str(self.objNum)}"

	class Meta:
		verbose_name = "Объект"
		verbose_name_plural = "Объекты"


class Country(models.Model):
	idCountry = models.AutoField(primary_key=True)
	countryName = models.CharField(max_length=125)

	def __str__(self):
		return self.countryName

	class Meta:
		verbose_name = "Страна"
		verbose_name_plural = "Страны"


class Region(models.Model):
	idRegion = models.AutoField(primary_key=True)
	regionName = models.CharField(max_length=255)

	def __str__(self):
		return self.regionName

	class Meta:
		verbose_name = "Регион"
		verbose_name_plural = "Регионы"


class City(models.Model):
	idCity = models.AutoField(primary_key=True)
	cityName = models.CharField(max_length=125)

	def __str__(self):
		return self.cityName

	class Meta:
		verbose_name = "Город"
		verbose_name_plural = "Города"



