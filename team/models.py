from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to="member/")
    awards = models.JSONField(default=list)
    roles = models.JSONField(default=list)
    description = models.TextField()
    
    def __str__(self):
        return f"hello  i am {self.name}:i am {self.roles}"
    
