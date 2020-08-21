from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from webapp.models import Task, Status, Types, TYPE_CHOICES, STATUS_CHOICES, Projects
from webapp.forms import TaskForm, BROWSER_DATETIME_FORMAT, SimpleSearchForm
from django.http import HttpResponseNotAllowed
from django.views.generic import View, TemplateView, FormView, ListView, DetailView
from .base_views import FormView as CustomFormView
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        tasks = project.tasks.all()
        context['tasks'] = tasks
        return context
