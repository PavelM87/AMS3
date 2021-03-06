# Generated by Django 3.2 on 2021-04-07 14:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AmsType',
            fields=[
                ('idType', models.AutoField(primary_key=True, serialize=False)),
                ('typeName', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Тип АМС',
                'verbose_name_plural': 'Типы АМС',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('idCity', models.AutoField(primary_key=True, serialize=False)),
                ('cityName', models.CharField(max_length=125)),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('idCountry', models.AutoField(primary_key=True, serialize=False)),
                ('countryName', models.CharField(max_length=125)),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('idRegion', models.AutoField(primary_key=True, serialize=False)),
                ('regionName', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Регион',
                'verbose_name_plural': 'Регионы',
            },
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('idObject', models.AutoField(primary_key=True, serialize=False)),
                ('objReg', models.CharField(blank=True, max_length=5, null=True)),
                ('objNum', models.IntegerField(blank=True, null=True)),
                ('objGeoLat', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
                ('objGeoLng', models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True)),
                ('objStatus', models.BooleanField(default=True)),
                ('objNote', models.TextField()),
                ('objAddress', models.CharField(blank=True, max_length=255, null=True)),
                ('objAmsSection', models.CharField(choices=[('square', 'Квадрат'), ('triangle', 'Треугольник'), ('circle', 'Круг')], default='Квадрат', max_length=8)),
                ('objFermType', models.CharField(choices=[('sq_ferm', 'ферма квадратная'), ('tr_ferm', 'ферма треугольная'), ('pipe', 'труба'), ('pillar', 'столб')], default='ферма квадратная', max_length=7)),
                ('sectionLength', models.IntegerField()),
                ('amsHeight', models.IntegerField()),
                ('signalSigns', models.BooleanField(default=True)),
                ('amsDeviation', models.DecimalField(decimal_places=2, max_digits=5)),
                ('amsFastenHeight', models.DecimalField(decimal_places=2, max_digits=4)),
                ('amsRopeDia', models.DecimalField(decimal_places=2, max_digits=5)),
                ('amsRopesQty', models.IntegerField()),
                ('amsTension', models.DecimalField(decimal_places=2, max_digits=5)),
                ('amsWaterproof', models.TextField(blank=True, null=True)),
                ('amsProducer', models.CharField(blank=True, max_length=255, null=True)),
                ('amsOperator', models.CharField(blank=True, max_length=255, null=True)),
                ('amsDocsDev', models.CharField(blank=True, max_length=255, null=True)),
                ('amsImgPlan', models.ImageField(blank=True, null=True, upload_to='')),
                ('amsImgEquip', models.ImageField(blank=True, null=True, upload_to='')),
                ('amsImgPhotos', models.ImageField(blank=True, null=True, upload_to='')),
                ('objDate', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('tblObjectscol', models.CharField(blank=True, max_length=45, null=True)),
                ('objAmsType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.amstype')),
                ('objCity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.city')),
                ('objCountry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.country')),
                ('objRegion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.region')),
            ],
            options={
                'verbose_name': 'Объект',
                'verbose_name_plural': 'Объекты',
            },
        ),
    ]
