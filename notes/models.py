from django.db import models


class Notes(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=8000, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


