from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from webapp.models import Task, Status, Types, TYPE_CHOICES, STATUS_CHOICES, Projects
from webapp.forms import TaskForm, ProjectForm
from django.http import HttpResponseNotAllowed
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.db.models import Q


class ProjectsIndex(ListView):
    template_name = 'project/index_project.html'
    context_object_name = 'projects'

    def get_queryset(self):
        data = Projects.objects.all()
        return data


class ProjectView(DetailView):
    template_name = 'project/project_view.html'
    model = Projects
    paginate_tasks_by = 2
    paginate_tasks_orphans = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks, page, is_paginated = self.paginate_tasks(self.object)
        context['tasks'] = tasks
        context['page_obj'] = page
        context['is_paginated'] = is_paginated
        return context

    def paginate_tasks(self, project):
        tasks = project.tasks.all().order_by('-created_at')
        if tasks.count() > 0:
            paginator = Paginator(tasks, self.paginate_tasks_by, orphans=self.paginate_tasks_orphans)
            page_number = self.request.GET.get('page', 1)
            page = paginator.get_page(page_number)
            is_paginated = paginator.num_pages > 1  # page.has_other_pages()
            return page.object_list, page, is_paginated
        else:
            return tasks, None, False



class ProjectCreateView(CreateView):
    template_name = 'project/project_create.html'
    form_class = ProjectForm
    model = Projects

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectUpdateView(UpdateView):
    template_name = 'project/project_update.html'
    form_class = ProjectForm
    model = Projects

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    template_name = 'project/project_delete.html'
    model = Projects
    success_url = reverse_lazy('projects_index')