# Generated by Django 3.2 on 2021-05-04 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_customuser_userrole'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='userEmail',
            field=models.EmailField(max_length=45, unique=True, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='userName',
            field=models.CharField(max_length=15, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='userRole',
            field=models.ForeignKey(default=3, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.role', verbose_name='Права пользователя'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='userSurname',
            field=models.CharField(max_length=45, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='userTel',
            field=models.CharField(max_length=15, verbose_name='Телефон'),
        ),
    ]
