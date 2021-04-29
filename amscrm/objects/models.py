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
	objReg = models.CharField(max_length=5, null=True, blank=True, verbose_name='Шифр / код объекта')
	objNum = models.IntegerField(null=True, blank=True, verbose_name='Альтернативный код')
	objGeoLat = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True, verbose_name='Широта')
	objGeoLng = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True, verbose_name='Долгота')
	objCountry = models.ForeignKey("Country", null=True, on_delete=models.SET_NULL, verbose_name='Страна')
	objRegion = models.ForeignKey("Region", null=True, on_delete=models.SET_NULL, verbose_name='Регион')
	objCity = models.ForeignKey("City", null=True, on_delete=models.SET_NULL, verbose_name='Город')
	objStatus = models.BooleanField(default=True, verbose_name='Статус')
	objNote = models.TextField(verbose_name='Примечание')
	objAddress = models.CharField(max_length=255, null=True, blank=True, verbose_name='Адрес')
	objAmsType = models.CharField(choices=AMS_TYPES, max_length=8, default='Квадрат', verbose_name='Тип фермы')
	objAmsSection = models.CharField(choices=AMS_SECTIONS, max_length=15, default='Квадрат', verbose_name='Тип секции')
	objFermType = models.CharField(choices=FERM_TYPE, max_length=7, default='ферма квадратная', verbose_name='Тип фермы')
	sectionLength = models.IntegerField(verbose_name='Длина секции')
	amsHeight = models.IntegerField(verbose_name='Высота АМС')
	signalSigns = models.BooleanField(default=True, verbose_name='Сигнальные огни')
	amsDeviation = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Отклонение')
	amsFastenHeight = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Высота крепления')
	amsRopeDia = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Диаметр каната')
	amsRopesQty = models.IntegerField(verbose_name='Количество канатов')
	amsTension = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Натяжения')
	amsWaterproof = models.TextField(null=True, blank=True, verbose_name='Гидроизоляция')
	amsProducer = models.CharField(max_length=255, null=True, blank=True, verbose_name='Изготовитель Объекта')
	amsOperator = models.CharField(max_length=255, null=True, blank=True, verbose_name='Наличие операторов связи на Объекте')
	amsDocsDev = models.CharField(max_length=255, null=True, blank=True, verbose_name='Разработчик проектной документации')
	amsImgPlan = models.ImageField(null=True, blank=True, verbose_name='Схема Объекта')
	amsImgEquip = models.ImageField(null=True, blank=True, verbose_name='Схема расположения оборудования на Объекте')
	amsImgPhotos = models.ImageField(null=True, blank=True, verbose_name='Фотографии Объекта')
	objDate = models.DateTimeField(default=timezone.now, null=True, blank=True, verbose_name='АдДатарес')
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



