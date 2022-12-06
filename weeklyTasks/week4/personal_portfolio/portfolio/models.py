from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField()

    def __str__(self) -> str:
        return self.title