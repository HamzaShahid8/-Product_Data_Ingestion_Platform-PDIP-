from django.db import models

# Create your models here.

class Product(models.Model):
    sku = models.CharField(max_length=150, unique=True)
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField()
    brand = models.CharField(max_length=150)
    
    def __str__(self):
        return self.sku
    
class ImportJob(models.Model):
    STATUS_CHOICES = [
        ('uploaded', 'Uploaded'),
        ('queued', 'Queued'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    file = models.FileField(upload_to='imports/')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='uploaded')
    total_rows = models.PositiveIntegerField(default=0)
    success_rows = models.PositiveIntegerField(default=0)
    failed_rows = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
class ImportError(models.Model):
    job = models.ForeignKey(ImportJob, on_delete=models.CASCADE, related_name='errors')
    row_number = models.IntegerField()
    message = models.TextField()