# Generated by Django 3.2 on 2021-04-07 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210407_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='userRole',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.role'),
        ),
    ]