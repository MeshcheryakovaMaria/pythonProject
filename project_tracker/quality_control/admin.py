from django.contrib import admin
from .models import BugReport, FeatureRequest

def change_status_bugreport(modeladmin, request, queryset):
    queryset.update(status='Resolved')
    change_status_bugreport.short_description = "Change status of selected bug reports"

def change_priority_featurerequest(modeladmin, request, queryset):
    queryset.update(priority='High')
    change_priority_featurerequest.short_description = "Change priority of selected feature requests"

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status', 'priority', 'project', 'task']
    list_filter = ['status', 'priority', 'project', 'task']
    search_fields = ['title', 'description']
    actions = [change_status_bugreport]
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'status', 'priority', 'project', 'task')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': (),
        }),
    )

@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status', 'priority', 'created_at', 'project', 'task']
    list_filter = ['status', 'priority', 'project', 'task']
    search_fields = ['title', 'description']
    actions = [change_priority_featurerequest]
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'status', 'priority', 'project', 'task')
        }),
    )
