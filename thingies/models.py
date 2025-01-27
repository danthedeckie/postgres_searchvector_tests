from django.db import models
from django.contrib.postgres.search import SearchVector

class Thing(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    search_vector = SearchVector()

    def save(self, *args, **kwargs):
        self.search_vector = SearchVector('title', 'subtitle', 'description')
        super().save(*args, **kwargs)
