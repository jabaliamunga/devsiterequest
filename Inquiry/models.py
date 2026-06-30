from django.db import models

class Inquiry(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    service = models.CharField(max_length=1000, blank=True, null=True)

    budget = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name

# Create your models here.
