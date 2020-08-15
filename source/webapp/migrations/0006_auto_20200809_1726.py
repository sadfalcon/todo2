# Generated by Django 2.2 on 2020-08-09 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20200804_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='types',
        ),
        migrations.AddField(
            model_name='task',
            name='types',
            field=models.ManyToManyField(blank=True, related_name='tasks', to='webapp.Types', verbose_name='Тип'),
        ),
    ]