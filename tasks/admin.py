from django.contrib import admin
from .models import Task, Attachment, Label


class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'start', 'end', 'comment')
    list_display_links = ('task', 'comment')
    search_fields = ('task', 'start')


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('picture',)
    list_display_links = ('picture',)
    search_fields = ('picture',)


admin.site.register(Task, TaskAdmin)
admin.site.register(Attachment, AttachmentAdmin)
admin.site.register(Label)
