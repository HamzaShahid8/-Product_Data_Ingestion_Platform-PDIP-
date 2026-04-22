from rest_framework import serializers
from .models import *

class ProductSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "sku", "title", "price", "stock", "description", "image_url", "brand"]
        
# only for validation not storing data
class ImportUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    
    def validate_file(self, value):
        if not value.name.endswith('.xlsx'):
            raise serializers.ValidationError('Only .xlsx files are allowed')
        return value
    
class ImportJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportJob
        fields = ["id", "status", "total_rows", "success_rows", "failed_rows", "created_at", 'processed_rows', 'processed_batches']
        
class ImportErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportError
        fields = ["row_number", "message"]