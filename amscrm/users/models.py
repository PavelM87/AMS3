from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    idUser = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=15, verbose_name='Имя')
    userSurname = models.CharField(max_length=45, verbose_name='Фамилия')
    userTel = models.CharField(max_length=15, verbose_name='Телефон')
    userEmail = models.EmailField(max_length=45, unique=True, verbose_name='Электронная почта')
    userRole = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True, default=3, verbose_name='Права пользователя')
    is_active = models.BooleanField(default=True, verbose_name='Статус')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'userEmail'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.userEmail

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Role(models.Model):
    idRole = models.AutoField(primary_key=True)
    roleName = models.CharField(max_length=45, null=True)

    def __str__(self):
        return self.roleName

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"


class Team(models.Model):
    member = models.ManyToManyField(CustomUser)

    def __str__(self):
        return f"{self.member.all()[0].userSurname}, {self.member.all()[1].userSurname} {self.id}"

    class Meta:
        verbose_name = "Бригада"
        verbose_name_plural = "Бригады"
        
