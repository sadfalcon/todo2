# Generated by Django 2.2 on 2020-08-15 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20200813_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Время изменения'),
        ),
    ]
