

#Class-Based Views
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from .models import BugReport, FeatureRequest
from django.shortcuts import render, redirect
from .forms import BugReportForm
from .forms import FeatureRequestForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404

# class IndexView(TemplateView):
#     template_name = 'quality_control/index.html'
#
# class BugReportListView(ListView):
#     model = BugReport
#     template_name = 'quality_control/bugreport_list.html'
#
# class FeatureRequestListView(ListView):
#     model = FeatureRequest
#     template_name = 'quality_control/featurerequest_list.html'
#
# class BugReportDetailView(DetailView):
#     pk_url_kwarg = "pk_id"
#     model = BugReport
#     template_name = 'quality_control/bugreport_detail.html'
#
# class FeatureRequestDetailView(DetailView):
#     pk_url_kwarg = "pk_id"
#     model = FeatureRequest
#     template_name = 'quality_control/featurerequest_detail.html'
#
# class BugReportCreateView(CreateView):
#     model = BugReport
#     template_name = 'quality_control/bug_report_form.html'
#     fields = '__all__'
#     success_url = reverse_lazy('quality_control:index')
#
# class FeatureRequestCreateView(CreateView):
#     model = FeatureRequest
#     template_name = 'quality_control/feature_request_form.html'
#     fields = '__all__'
#     success_url = reverse_lazy('quality_control:index')
# class BugReportUpdateView(UpdateView):
#     model = BugReport
#     form_class = BugReportForm
#     template_name = 'quality_control/bugreport_update.html'
#     pk_url_kwarg = 'pk_id'  # Используем 'pk' вместо 'all'
#     success_url = reverse_lazy('quality_control:index')
#     def get_success_url(self):
#         return reverse_lazy('quality_control:bugreport_detail',
#                             kwargs={'pk_id': self.object.project.id, 'pk_id': self.object.id})
#
# class FeatureRequestUpdateView(UpdateView):
#     model = FeatureRequest
#     form_class = FeatureRequestForm
#     template_name = 'quality_control/featurerequest_update.html'
#     pk_url_kwarg = 'pk_id'  # Используем 'pk' вместо 'all'
#     success_url = reverse_lazy('quality_control:index')
#     def get_success_url(self):
#         return reverse_lazy('quality_control:featurerequest_detail',
#                             kwargs={'pk_id': self.object.project.id, 'pk_id': self.object.id})
#
# class BugReportDeleteView(DeleteView):
#     model = BugReport
#     pk_url_kwarg = 'pk_id'
#     def get_success_url(self):
#         return reverse_lazy('quality_control:bugreport_list')
#
# class FeatureRequestDeleteView(DeleteView):
#     model = FeatureRequest
#     pk_url_kwarg = 'pk_id'
#     def get_success_url(self):
#         return reverse_lazy('quality_control:featurerequest_list')


#Function-Based Views
def index(request):
    return render(request, 'quality_control/index.html')

def bugreport_list(request):
    bugreports = BugReport.objects.all()
    return render(request, 'quality_control/bugreport_list.html', {'bugreport_list': bugreports})
def featurerequest_list(request):
    featurerequests = FeatureRequest.objects.all()
    return render(request, 'quality_control/featurerequest_list.html', {'featurerequest_list': featurerequests})

def bugreport_detail(request, pk_id):
    bugreport = get_object_or_404(BugReport, pk=pk_id)
    return render(request, 'quality_control/bugreport_detail.html', {'bugreport': bugreport, 'pk_id': pk_id})

def featurerequest_detail(request, pk_id):
    featurerequest = get_object_or_404(FeatureRequest, pk=pk_id)
    return render(request, 'quality_control/featurerequest_detail.html', {'featurerequest': featurerequest, 'pk_id': pk_id})

def bugreport_create(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:index')  # Перенаправление на главную страницу после сохранения формы
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html.', {'form': form})
def featurerequest_create(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:index')
    else:
       form = FeatureRequestForm()
       return render(request, 'quality_control/feature_request_form.html', {'form': form})
def bugreport_update(request, pk_id):
    bug_report = get_object_or_404(BugReport, pk=pk_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug_report)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bugreport_detail', pk_id=pk_id)
    else:
        form = BugReportForm(instance=bug_report)
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

def featurerequest_update(request, pk_id):
    feature_request = get_object_or_404(FeatureRequest, pk=pk_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature_request)
        if form.is_valid():
            form.save()
            return redirect('quality_control:featurerequest_detail', pk_id=pk_id)
    else:
        form = FeatureRequestForm(instance=feature_request)
    return render(request, 'quality_control/feature_request_form.html', {'form': form})

def bugreport_delete(request, bugreport_id):
    bug_report = get_object_or_404(BugReport, pk=bugreport_id)
    bug_report.delete()
    return redirect('quality_control:bugreport_list')

def featurerequest_delete(request, pk_id):
    feature_request = get_object_or_404(FeatureRequest, pk=pk_id)
    if request.method == 'POST':
        feature_request.delete()
        return redirect('quality_control:featurerequest_list')
    return render(request, 'quality_control/featurerequest_confirm_delete.html', {'feature_request': feature_request})
def featurerequest_delete(request, featurerequest_id):
    feature_request = get_object_or_404(FeatureRequest, pk=featurerequest_id)
    feature_request.delete()
    return redirect('quality_control:featurerequest_list')
