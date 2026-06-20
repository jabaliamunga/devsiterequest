from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=150, blank=True, null=True)
    role = models.CharField(max_length=150, blank=True, null=True)
    testimonial_image = models.ImageField(upload_to="../images/testimonials/")
    remarks = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rate from 1 to 5"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}"
