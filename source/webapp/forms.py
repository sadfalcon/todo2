from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
from .models import Task, Projects
#default_types = TYPE_CHOICES[0][0]
#default_status = STATUS_CHOICES[0][0]
BROWSER_DATETIME_FORMAT = '%d.%m.%Y %H:%M'

@deconstructible
class MinLengthValidator(BaseValidator):
    message = 'Value "%(value)s" has length of %(show_value)d! It should be at least %(limit_value)d symbols long!'
    code = 'too_short'

    def compare(self, value, limit):
        return value < limit

    def clean(self, value):
        return len(value)

@deconstructible
class MaxLengthValidator(BaseValidator):
    message = 'Ensure this value has at most %(limit_value)d character (it has %(show_value)d).'
    code = 'max_length'

    def compare(self, a, b):
        return a > b

    def clean(self, x):
        return len(x)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'types']

    def clean(self):
        cleaned_data = super().clean()
        errors = []
        summary = cleaned_data.get('summary')
        description = cleaned_data.get('description')
        if summary and description and summary == description:
            errors.append(ValidationError("Description of the task should not duplicate it's summary!"))
        if errors:
            raise ValidationError(errors)
        return cleaned_data

class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['name', 'description', 'start_date', 'end_date']