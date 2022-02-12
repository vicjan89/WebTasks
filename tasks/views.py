from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Task, Label, Attachment
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

class TaskDetaiView(DetailView):
    model = Task
    template_name = 'tasks/detail.html'

def index(request):
    tasks_list = Task.objects.all()
    lbls = Label.objects.all()
    context = {
        'tasks_list': tasks_list,
        'lbls': lbls
    }
    return render(request, 'tasks/index.html', context)

def by_label(request, label_id):
    lbls = Label.objects.all()
    current_label = Label.objects.get(pk=label_id)
    tsk = current_label.task_set.all()
    context = {'tsk': tsk, 'lbls': lbls, 'current_label': current_label}
    return render(request, 'tasks/by_label.html', context)

def attachment(request):
    attach = Attachment.objects.all()
    context = {'attach': attach}
    return render(request, 'tasks/attachment.html', context)

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['label'] = Label.objects.all()
        return context

class TaskDeleteView(DeleteView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['label'] = Label.objects.all()
        return context