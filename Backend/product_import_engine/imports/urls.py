from django.urls import path
from .views import *

urlpatterns = [
    
    # upload excel file
    path('products/', UploadImportView.as_view(), name='upload-import'),
    
    # get job summary and status
    path('<int:job_id>/', JobDetailView.as_view(), name='job-detail'),
    
    # row-level errors
    path('<int:job_id>/errors/', JobErrorsView.as_view(), name='job-errors'),
    
    # Dashboard
    path('dashboard/import-jobs/', ImportJobDashboardView.as_view(), name='import_jobs'),
    
    path('dashboard/import-jobs/<int:job_id>/', ImportJobDetailView.as_view(), name='import_jobs_id'),
    
    path('dashboard/import-jobs/<int:job_id>/errors/', ImportJobErrorView.as_view(), name='import_jobs_errors'),
]