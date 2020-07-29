from django import forms
from .models import status_choices


default_status = status_choices[0][0]

class ArticleForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label='Описание')
    full_description = forms.CharField(max_length=3000, label='Полное описание', widget=forms.Textarea)
    date_end = forms.DateField(label='Дата выполнения', required=False, widget=forms.DateTimeInput(attrs={'type':'date'}))
    status = forms.ChoiceField(choices=status_choices, initial=default_status, label='статус')
