from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Project, Task
from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView
from .forms import FeedbackForm
from django.shortcuts import render, redirect
from .forms import ProjectForm
from django.forms import ModelForm
from .forms import TaskForm
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


# Class-Based Views (CBV)
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tasks/index.html')

class ProjectsListView(ListView):
    model = Project
    template_name = 'tasks/projects_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects_list'] = context.pop('project_list')  # Изменяем ключ в контексте
        return context


class ProjectDetailView(DetailView):
    model = Project
    pk_url_kwarg = 'project_id'
    template_name = 'tasks/project_detail.html'

class TaskDetailView(DetailView):
    model = Task
    pk_url_kwarg = 'task_id'
    template_name = 'tasks/task_detail.html'
class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'tasks/project_update.html'
    pk_url_kwarg = 'project_id'
    success_url = reverse_lazy('tasks:projects_list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_update.html'
    pk_url_kwarg = 'task_id'

    def get_success_url(self):
        return reverse_lazy('tasks:task_detail',
                            kwargs={'project_id': self.object.project.id, 'task_id': self.object.id})

class ProjectDeleteView(DeleteView):
    model = Project
    pk_url_kwarg = 'project_id'
    success_url = reverse_lazy('tasks:projects_list')
    template_name = 'tasks/project_confirm_delete.html'
class TaskDeleteView(DeleteView):
    model = Task
    pk_url_kwarg = 'task_id'

    def get_success_url(self):
        return reverse_lazy('tasks:project_detail', kwargs={'project_id': self.object.project.id})

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'tasks/project_create.html'
    success_url = reverse_lazy('tasks:projects_list')

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/add_task.html'

    def form_valid(self, form):
        form.instance.project = get_object_or_404(Project, pk=self.kwargs['project_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tasks:project_detail', kwargs={'project_id': self.kwargs['project_id']})


# #Function-Based Views (FBV)
# def update_project(request, project_id):
#     project = get_object_or_404(Project, pk=project_id)
#     if request.method == 'POST':
#         form = ProjectForm(request.POST, instance=project)
#         if form.is_valid():
#             form.save()
#             return redirect('tasks:project_detail', project_id=project.id)
#     else:
#         form = ProjectForm(instance=project)
#     return render(request, 'tasks/project_update.html', {'form': form, 'project': project})
# def update_task(request, project_id, task_id):
#     task = get_object_or_404(Task, pk=task_id)
#     if request.method == 'POST':
#         form = TaskForm(request.POST, instance=task)
#         if form.is_valid():
#             form.save()
#             return redirect('tasks:task_detail', project_id=project_id, task_id=task.id)
#     else:
#         form = TaskForm(instance=task)
#     return render(request, 'tasks/task_update.html', {'form': form, 'task': task})

# def delete_project(request, project_id):
#     project = get_object_or_404(Project, pk=project_id)
#     project.delete()
#     return redirect('tasks:projects_list')
#
# def delete_task(request, project_id, task_id):
#     task = get_object_or_404(Task, pk=task_id)
#     task.delete()
#     return redirect('tasks:project_detail', project_id=project_id)


