from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from .models import Task, Label
from .forms import TaskForm
from django.urls import reverse_lazy


class TaskCreateView(CreateView):
    template_name = 'tasks/create.html'
    form_class = TaskForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['label'] = Label.objects.all()
        return context

def index(request):
    tasks_list = Task.objects.all()
    lbls = Label.objects.all()
    context = {
        'tasks_list': tasks_list,
        'lbls': lbls
    }
    return render(request, 'tasks/index.html', context)

def by_label(request, label_id):
    tsk = Task.objects.filter(label=label_id)
    lbls = Label.objects.all()
    current_label = Label.objects.get(pk=label_id)
    context = {'tsk': tsk, 'lbls': lbls, 'current_label': current_label}
    return render(request, 'tasks/by_label.html', context)
