from django.contrib import admin
from webapp.models import Task, Status, Types   # импортируем модель

class TaskAdmin(admin.ModelAdmin):
    list_filter = ('status', 'types')
    list_display = ('pk', 'summary', 'description', 'status')
    list_display_links = ('pk', 'summary')
    search_fields = ('summary',)


admin.site.register(Task, TaskAdmin)
admin.site.register(Status)
admin.site.register(Types)
