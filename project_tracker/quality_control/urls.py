#Function-Based Views
from django.urls import path
from . import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='index'),
    path('bugreports/', views.bugreport_list, name='bugreport_list'),
    path('bugreports/<int:pk_id>/', views.bugreport_detail, name='bugreport_detail'),
    path('featurerequests/', views.featurerequest_list, name='featurerequest_list'),
    path('featurerequests/<int:pk_id>/', views.featurerequest_detail, name='featurerequest_detail'),
    path('bugreport_create/', views.bugreport_create, name='bugreport_create'),
    path('featurerequest_create/', views.featurerequest_create, name='featurerequest_create'),
    path('bugreports/<int:pk_id>/update/', views.bugreport_update, name='bugreport_update'),
    path('bugreports/<int:bugreport_id>/delete/', views.bugreport_delete, name='bugreport_delete'),
    path('featurerequests/<int:pk_id>/update/', views.featurerequest_update, name='featurerequest_update'),
    path('featurerequests/<int:featurerequest_id>/delete/', views.featurerequest_delete, name='featurerequest_delete'),
   ]


# #Class-Based Views
#
# from django.urls import path
# from . import views
#
#
# app_name = 'quality_control'
#
# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('bugreports/', views.BugReportListView.as_view(), name='bugreport_list'),
#     path('featurerequests/', views.FeatureRequestListView.as_view(), name='featurerequest_list'),
#     path('bugreports/<int:pk_id>/', views.BugReportDetailView.as_view(), name='bugreport_detail'),
#     path('featurerequests/<int:pk_id>/', views.FeatureRequestDetailView.as_view(), name='featurerequest_detail'),
#     path('featurerequests/create/', views.FeatureRequestCreateView.as_view(), name='featurerequest_create'),
#     path('bugreports/create/', views.BugReportCreateView.as_view(), name='bugreport_create'),
#     path('bugreports/<int:pk_id>/update/', views.BugReportUpdateView.as_view(), name='bugreport_update'),
#     path('bugreports/<int:pk_id>/delete/', views.BugReportDeleteView.as_view(), name='bugreport_delete'),
#     path('featurerequests/<int:pk_id>/update/', views.FeatureRequestUpdateView.as_view(), name='featurerequest_update'),
#     path('featurerequests/<int:pk_id>/delete/', views.FeatureRequestDeleteView.as_view(), name='featurerequest_delete'),
#     ]