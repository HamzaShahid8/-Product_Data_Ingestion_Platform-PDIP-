from django.shortcuts import render
from .tasks import *
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.

# UPLOAD EXCEL FILE
class UploadImportView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        consumes=['multipart/form-data'],
        manual_parameters=[
            openapi.Parameter(
                'file',
                openapi.IN_FORM,
                type=openapi.TYPE_FILE,
                required=True,
                description="Upload Excel file (.xlsx)"
            )
        ]
    )
    def post(self, request):
        serializer = ImportUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        file = serializer.validated_data["file"]

        job = ImportJob.objects.create(
            file=file,
            status="queued"
        )

        # send to celery
        process_import.delay(job.id)

        return Response(
            {
                "message": "File uploaded successfully",
                "job_id": job.id
            },
            status=status.HTTP_201_CREATED
        )


# JOB STATUS / SUMMARY
class JobDetailView(APIView):
    def get(self, request, job_id):
        try:
            job = ImportJob.objects.get(id=job_id)
        except ImportJob.DoesNotExist:
            return Response(
                {"error": "Job not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ImportJobSerializer(job)
        return Response(serializer.data)


# 3. JOB ERRORS LIST
class JobErrorsView(APIView):
    def get(self, request, job_id):
        try:
            job = ImportJob.objects.get(id=job_id)
        except ImportJob.DoesNotExist:
            return Response(
                {"error": "Job not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        errors = ImportError.objects.filter(job=job)

        serializer = ImportErrorSerializer(errors, many=True)

        return Response(
            {
                "job_id": job.id,
                "errors": serializer.data
            }
        )