from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from webapp.models import Task, Status, Types, TYPE_CHOICES, STATUS_CHOICES, Projects
from webapp.forms import TaskForm, BROWSER_DATETIME_FORMAT, SimpleSearchForm
from django.http import HttpResponseNotAllowed
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.utils.timezone import make_naive
from .base_views import FormView as CustomFormView
from django.db.models import Q


# Create your views here.

class IndexView(ListView):
    template_name = 'task/index.html'
    context_object_name = 'tasks'
    paginate_by = 5
    paginate_orphans = 0

    def get_context_data(self, *, object_list=None, **kwargs):
        form = SimpleSearchForm(data=self.request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            kwargs['search'] = search
        kwargs['form'] = form
        return super().get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        data = Task.objects.all()

        # if not self.request.GET.get('is_admin', None):
        # data = Task.objects.filter(status='moderated')

        # http://localhost:8000/?search=ygjkjhg
        form = SimpleSearchForm(data=self.request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            if search:
                data = data.filter(Q(summary__icontains=search) | Q(description__icontains=search))

        return data.order_by('-created_at')


class TaskView(TemplateView):
    template_name = 'task/task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        context = {'task': task}
        return context


class ProjectTaskCreateView(CreateView):
    model = Task
    template_name = 'task/task_create2.html'
    form_class = TaskForm

    def form_valid(self, form):
        project = get_object_or_404(Projects, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        form.save_m2m()
        return redirect('project_view', pk=project.pk)


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task/task_update.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.project.pk})


class TaskDeleteView(DeleteView):
    model = Task

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.project.pk})
