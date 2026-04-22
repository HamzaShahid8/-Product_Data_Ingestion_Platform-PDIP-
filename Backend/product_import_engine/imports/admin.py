from django.contrib import admin
from .models import *


# PRODUCT ADMIN
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("sku", "title", "price", "stock", "brand")
    search_fields = ("sku", "title", "brand")
    list_filter = ("brand",)
    ordering = ("-id",)

# IMPORT ERROR INLINE
class ImportErrorInline(admin.TabularInline):
    model = ImportError
    extra = 0
    readonly_fields = ("row_number", "message")
    can_delete = False

# IMPORT JOB ADMIN
@admin.register(ImportJob)
class ImportJobAdmin(admin.ModelAdmin):
    list_display = ("id", "status", "total_rows", "success_rows", "failed_rows", "processed_rows", "processed_batches", "created_at")
    list_filter = ("status", "created_at")
    readonly_fields = ("status", "total_rows", "success_rows", "failed_rows", "created_at")
    search_fields = ("id",)
    ordering = ("-created_at",)

# IMPORT ERROR ADMIN
@admin.register(ImportError)
class ImportErrorAdmin(admin.ModelAdmin):
    list_display = ("job", "row_number", "message")
    list_filter = ("job",)
    search_fields = ("message",)