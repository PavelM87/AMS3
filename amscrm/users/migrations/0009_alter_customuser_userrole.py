# Generated by Django 3.2 on 2021-04-17 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='userRole',
            field=models.ForeignKey(default=3, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.role'),
        ),
    ]
