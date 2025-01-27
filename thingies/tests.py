from django.test import TestCase

from .models import Thing

class ThingModelTest(TestCase):
    def setUp(self):
        Thing.objects.create(title="Test Title", subtitle="Test Subtitle", description="Test Description")

    def test_search_title(self):
        results = Thing.objects.search("Title")
        self.assertEqual(results.count(), 1)

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
