from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Task
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, CreateView, UpdateView

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = Task.objects.filter(title__contains=search_input)
        else:
            context['tasks'] = Task.objects.all()

        context['count'] = context['tasks'].filter(complete=False).count()
        context['search_input'] = search_input

        return context

class TaskDetail(DetailView):
    model = Task
    context_object_name ='task'
    template_name = 'todolist/task.html'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model = Task 
    fields='__all__'
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task
    context_object_name='task'
    success_url = reverse_lazy('tasks')

