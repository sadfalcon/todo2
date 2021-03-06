# Generated by Django 2.2 on 2020-08-04 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_article_full_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Выполнено')], default='new', max_length=15, verbose_name='Модерация')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=3000, verbose_name='Описание')),
                ('description', models.TextField(blank=True, default=None, max_length=3000, null=True, verbose_name='Полное описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='webapp.Status', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('task', 'Задача'), ('bug', 'Ошибка'), ('enhancement', 'Улучшение')], default='new', max_length=15, verbose_name='Модерация')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
            },
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.AddField(
            model_name='task',
            name='types',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='webapp.Types', verbose_name='Тип'),
        ),
    ]
