from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    technologies = models.JSONField(default=list,blank=True)
    thumbnails = models.ImageField(upload_to="images/", blank=True)
    project_url = models.URLField()
    github_url = models.URLField()
    
    class Meta:
        ordering = ["-id"]
    
    
    def __str__(self):
        return f"{self.title}"
