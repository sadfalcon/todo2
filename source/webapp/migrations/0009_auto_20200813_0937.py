# Generated by Django 2.2 on 2020-08-13 09:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20200809_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='summary',
            field=models.CharField(max_length=3000, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(3000)], verbose_name='Описание'),
        ),
    ]
