from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Task, Label, Attachment
from .forms import TaskForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = 'tasks/create.html'
    form_class = TaskForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['label'] = Label.objects.all()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)

class TaskDetaiView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/detail.html'

@login_required
def index(request):
        print(request.user)
        tasks_list = Task.objects.filter(user=request.user)
        lbls = Label.objects.all()
        context = {
            'tasks_list': tasks_list,
            'lbls': lbls
        }
        return render(request, 'tasks/index.html', context)

@login_required
def by_label(request, label_id):
    lbls = Label.objects.all()
    current_label = Label.objects.get(pk=label_id)
    tsk = current_label.task_set.all()
    context = {'tsk': tsk, 'lbls': lbls, 'current_label': current_label}
    return render(request, 'tasks/by_label.html', context)

@login_required
def attachment(request):
    attach = Attachment.objects.all()
    context = {'attach': attach}
    return render(request, 'tasks/attachment.html', context)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['label'] = Label.objects.all()
        return context

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['label'] = Label.objects.all()
        return context