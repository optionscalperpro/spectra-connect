from django.db import models
from django.contrib.auth.models import User

class OperationsFile(models.Model):
    file_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    link = models.URLField()
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    last_updated = models.DateTimeField()

    def __str__(self):
        return self.file_name