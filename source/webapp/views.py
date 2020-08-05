from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from webapp.models import Task, Status, Types, TYPE_CHOICES, STATUS_CHOICES
from webapp.forms import TaskForm, BROWSER_DATETIME_FORMAT
from django.http import HttpResponseNotAllowed
from django.views.generic import View, TemplateView
from django.utils.timezone import make_naive
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


class TaskCreateView(View):
    def get(self, request):
        return render(request, 'task_create.html', context={
            'form': TaskForm()
        })
    def post(self, request):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            # article = Article.objects.create(**form.cleaned_data)
            task = Task.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                types=form.cleaned_data['types'],
                created_at=form.cleaned_data['created_at']
            )
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'task_create.html', context={
                'form': form
            })


class TaskView(TemplateView):
    template_name = 'task_view.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        context = {'task': task}
        return context

class TaskUpdateView(TemplateView):
    template_name = 'task_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(initial={'summary': task.description,
                                        'description': task.description,
                                        'status': task.status,
                                        'types': task.types,
                                        'created_at': make_naive(task.created_at).strftime(BROWSER_DATETIME_FORMAT)})
        context['task'] = task
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(data=request.POST)
        if form.is_valid():
            # article = Article.objects.create(**form.cleaned_data)
            task.summary = form.cleaned_data['summary']
            task.description = form.cleaned_data['description']
            task.status = form.cleaned_data['status']
            task.types = form.cleaned_data['types']
            task.created_at = form.cleaned_data['created_at']
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return self.render_to_response({
                'task': task,
                'form': form
            })

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
