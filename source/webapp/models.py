from django.db import models
from datetime import datetime, date
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils import timezone


# Create your models here.
STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Выполнено')]
TYPE_CHOICES = [('task', 'Задача'), ('bug', 'Ошибка'),  ('enhancement', 'Улучшение')]


class Task(models.Model):
    summary = models.CharField(max_length=3000, null=False, blank=False, verbose_name='Описание', validators=[MinLengthValidator(10), MaxLengthValidator(3000)])
    description = models.TextField(max_length=3000, null=True, blank=True, default=None, verbose_name='Полное описание')
    status = models.ForeignKey('webapp.Status', related_name='tasks',
                                on_delete=models.CASCADE, verbose_name='Статус')
    types = models.ManyToManyField('webapp.Types', related_name='tasks', blank=True, verbose_name='Тип')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    project = models.ForeignKey('webapp.Projects', related_name='tasks',
                                on_delete=models.CASCADE, verbose_name='Проект')


    def __str__(self):
        return "{}. {}".format(self.pk, self.summary)


    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class Status(models.Model):
    name = models.CharField(max_length=15, choices=STATUS_CHOICES, default='new', verbose_name='Модерация')

    def __str__(self):
        return "{}. {}".format(self.pk, self.name)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Types(models.Model):
    name = models.CharField(max_length=15, choices=TYPE_CHOICES, default='new', verbose_name='Модерация')

    def __str__(self):
        return "{}. {}".format(self.pk, self.name)

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Projects(models.Model):
    start_date = models.DateField(verbose_name='Время создания')
    end_date = models.DateField(null=True, blank=True, verbose_name='Время окончания')
    name = models.CharField(max_length=300, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание')

    def __str__(self):
        return "{}. {}".format(self.pk, self.name)


    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'







