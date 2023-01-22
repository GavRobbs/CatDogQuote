from django.db import models
import os

class Quote(models.Model):
    text = models.TextField(null=False, blank=False)
    author=models.CharField(max_length=255, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.author} - {self.text[:32]}"