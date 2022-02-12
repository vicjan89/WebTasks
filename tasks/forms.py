from django.forms import ModelForm, Textarea, SelectDateWidget, SplitDateTimeWidget, CheckboxSelectMultiple

from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('task', 'start', 'end', 'comment', 'repeat_mode', 'priority', 'duration', 'hard', 'progress',
                  'label', 'attachment')
        widgets = {
            'task': Textarea(attrs={'cols': 80, 'rows': 2}),
            'comment': Textarea(attrs={'cols': 80, 'rows': 2}),
            'label': CheckboxSelectMultiple(),
            'attachment': CheckboxSelectMultiple()
        }