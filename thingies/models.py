from django.db import models
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


class ThingQuerySet(models.QuerySet):
    def search(self, query):
        vector = SearchVector("title", "subtitle", "description")
        query = SearchQuery(query)
        return self.annotate(
            rank=SearchRank(vector, query)
        ).filter(search=query).order_by('-rank')


class Thing(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    search_vector = SearchVector()

    objects = ThingQuerySet.as_manager()

    def save(self, *args, **kwargs):
        self.search_vector = SearchVector("title", "subtitle", "description")
        super().save(*args, **kwargs)
