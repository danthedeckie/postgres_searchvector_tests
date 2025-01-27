from django.db import models
from django.db.models import F
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
            self.annotate(
                rank=SearchRank(
                    F("search_vector"),
                    query,
                    # Set the weights for each letter D,C,B,A
                    weights=[0.1, 0.2, 0.3, 1.0],
                    # Don't normalize by document-length:
                    normalization=0,
                )
            )
            # Only include results with any kind of match:
            .filter(rank__gt=0.00001)
            # Order by closest match:
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
            search_vector=SearchVector("title", weight="A")
            + SearchVector("subtitle", weight="B")
            + SearchVector("description", weight="C")
        )
