from django.db import models
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchVectorField,
)


class ThingQuerySet(models.QuerySet):
    def search(self, query):
        query = SearchQuery(query)
        return (
            self.annotate(rank=SearchRank("search_vector", query))
            .filter(rank__gt=0.00001)
            .order_by("-rank")
        )


class Thing(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    search_vector = SearchVectorField()

    objects = ThingQuerySet.as_manager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        Thing.objects.filter(pk=self.pk).update(
            search_vector=SearchVector("title", "subtitle", "description")
        )
