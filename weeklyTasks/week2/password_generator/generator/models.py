from django.db import models

class Password(models.Model):
    passwords = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.passwords
