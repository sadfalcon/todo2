from django.db import models
from datetime import datetime, date

# Create your models here.
STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Выполнено')]
TYPE_CHOICES = [('task', 'Задача'), ('bug', 'Ошибка'),  ('enhancement', 'Улучшение')]


class Task(models.Model):
    summary = models.CharField(max_length=3000, null=False, blank=False, verbose_name='Описание')
    description = models.TextField(max_length=3000, null=True, blank=True, default=None, verbose_name='Полное описание')
    status = models.ForeignKey('webapp.Status', related_name='tasks',
                                on_delete=models.CASCADE, verbose_name='Статус')
    types = models.ForeignKey('webapp.Types', related_name='tasks',
                               on_delete=models.CASCADE, verbose_name='Тип')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')


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









