from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from webapp.models import Task, Status, Types, TYPE_CHOICES, STATUS_CHOICES
from webapp.forms import TaskForm, BROWSER_DATETIME_FORMAT
from django.http import HttpResponseNotAllowed
from django.views.generic import View, TemplateView, FormView
from django.utils.timezone import make_naive
from .base_views import FormView as CustomFormView
# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        tasks = Task.objects.all()
        context = {
            'tasks': tasks
        }
        return context

class TaskCreateView(CustomFormView):
    template_name = 'task_create.html'
    form_class = TaskForm

    def form_valid(self, form):
        data = {}
        types = form.cleaned_data.pop('types')
        for key, value in form.cleaned_data.items():
            if value is not None:
                data[key] = value
        self.task = Task.objects.create(**data)
        self.task.types.set(types)
        return super().form_valid(form)

    def get_redirect_url(self):
        return reverse('task_view', kwargs={'pk': self.task.pk})




class TaskView(TemplateView):
    template_name = 'task_view.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        context = {'task': task}
        return context


class TaskUpdateView(FormView):
    template_name = 'task_update.html'
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def get_initial(self):
        initial = {}
        for key in 'summary', 'description', 'status', 'types':
            initial[key] = getattr(self.task, key)
        initial['created_at'] = make_naive(self.task.created_at)\
            .strftime(BROWSER_DATETIME_FORMAT)
        initial['types'] = self.task.types.all()
        return initial

    def form_valid(self, form):
        types = form.cleaned_data.pop('types')
        for key, value in form.cleaned_data.items():
            if value is not None:
                setattr(self.task, key, value)
        self.task.save()
        self.task.types.set(types)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.task.pk})

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Task, pk=pk)


class TaskDeleteView(TemplateView):
    template_name = 'delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        context = {'task': task}
        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('index')
