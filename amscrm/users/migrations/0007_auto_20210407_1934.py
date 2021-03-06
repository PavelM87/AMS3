# Generated by Django 3.2 on 2021-04-07 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_customuser_userrole'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='userRole',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.SET_DEFAULT, to='users.role'),
        ),
        migrations.AlterField(
            model_name='role',
            name='roleName',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
