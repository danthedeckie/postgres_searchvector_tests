from django.test import TestCase

from .models import Thing


class ThingModelTest(TestCase):
    def setUp(self):
        Thing.objects.create(
            title="Test Title", subtitle="Test Subtitle", description="Test Description"
        )

    def test_search_subtitle(self):
        results = Thing.objects.search("Subtitle")
        self.assertEqual(results.count(), 1)

    def test_search_description(self):
        results = Thing.objects.search("Description")
        self.assertEqual(results.count(), 1)

    def test_search_no_match(self):
        results = Thing.objects.search("Nonexistent")
        self.assertEqual(results.count(), 0)
        results = Thing.objects.search("Test")
        self.assertEqual(results.count(), 1)


class ThingModelOrderingTest(TestCase):
    def setUp(self):
        Thing.objects.create(
            title="Nope", subtitle="Keyword in Subtitle", description="Nope"
        )
        Thing.objects.create(
            title="Other",
            subtitle="Things",
            description="Keyword in Description",
        )
        Thing.objects.create(
            title="Keyword in Title", subtitle="Stuff", description="Other"
        )


    def test_search_ordering(self):
        results = Thing.objects.search("Keyword")
        self.assertEqual(results[0].title, "Keyword in Title")
        self.assertEqual(results[1].subtitle, "Keyword in Subtitle")
        self.assertEqual(results[2].description, "Keyword in Description")
