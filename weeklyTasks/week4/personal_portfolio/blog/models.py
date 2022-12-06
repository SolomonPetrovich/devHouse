from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField(auto_now=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title