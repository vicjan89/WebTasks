from django.forms import ModelForm

from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('task', 'start', 'end', 'comment', 'repeat_mode', 'priority', 'duration', 'hard', 'progress',
                  'label', 'attachment')