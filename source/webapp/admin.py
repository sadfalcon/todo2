from django.contrib import admin
from webapp.models import Task, Status, Types, Projects  # импортируем модель

class TaskAdmin(admin.ModelAdmin):
    list_filter = ('status', 'types')
    list_display = ('pk', 'summary', 'description', 'status')
    list_display_links = ('pk', 'summary')
    search_fields = ('summary',)

class ProjectsAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('pk', 'name', 'description',)
    list_display_links = ('pk', 'name')
    search_fields = ('name',)


admin.site.register(Task, TaskAdmin)
admin.site.register(Status)
admin.site.register(Types)
admin.site.register(Projects, ProjectsAdmin)
