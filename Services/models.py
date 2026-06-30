from django.db import models


class Services(models.Model):
    title = models.CharField(max_length=255)
    icon =  models.CharField(max_length=30)
    description = models.CharField(max_length=500)


    def __str__(self):
        return f"{self.title}, {self.description}"
    
    

# Create your models here.
