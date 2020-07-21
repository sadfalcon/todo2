from django.db import models

# Create your models here.
status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

class Article(models.Model):
    description = models.CharField(max_length=3000, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length=3000, null=False, blank=False, verbose_name='Статус', default='new' ,choices=status_choices)
    date_end = models.DateField(verbose_name='Дата выполнения')


    def __str__(self):
        return "{}. {}".format(self.pk, self.description)