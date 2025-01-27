from django.db import models
from django.contrib.postgres.search import SearchVector, SearchQuery

class ThingQuerySet(models.QuerySet):
    def search(self, query):
        return self.annotate(search=SearchVector('title', 'subtitle', 'description')).filter(search=SearchQuery(query))
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    search_vector = SearchVector()

    objects = ThingQuerySet.as_manager()

    def save(self, *args, **kwargs):
        self.search_vector = SearchVector('title', 'subtitle', 'description')
        super().save(*args, **kwargs)
