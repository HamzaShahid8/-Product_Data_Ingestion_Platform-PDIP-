from django.urls import path
from .views import *

urlpatterns = [
    
    # upload excel file
    path('products/', UploadImportView.as_view(), name='upload-import'),
    
    # get job summary and status
    path('<int:job_id>/', JobDetailView.as_view(), name='job-detail'),
    
    # row-level errors
    path('<int:job_id>/errors/', JobErrorsView.as_view(), name='job-errors'),
]