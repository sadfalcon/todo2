from django import forms
from .models import STATUS_CHOICES, TYPE_CHOICES, Status, Types

BROWSER_DATETIME_FORMAT = '%Y-%m-%dT%H:%M'
default_types = TYPE_CHOICES[0][0]
default_status = STATUS_CHOICES[0][0]

class TaskForm(forms.Form):
    summary = forms.CharField(max_length=3000, required=True, label='Описание')
    description = forms.CharField(max_length=3000, label='Полное описание', widget=forms.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), initial=default_status, label='Статус')
    types = forms.ModelMultipleChoiceField(queryset=Types.objects.all(), initial=default_types, label='Тип')
    created_at = forms.DateTimeField(required=False, label='Время создания',
                                     input_formats=['%Y-%m-%d', BROWSER_DATETIME_FORMAT,
                                                    '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M',
                                                    '%Y-%m-%d %H:%M:%S'],
                                     widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))