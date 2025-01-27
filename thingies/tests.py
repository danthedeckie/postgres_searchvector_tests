from django.test import TestCase

from .models import Thing

class ThingModelTest(TestCase):
    def setUp(self):
        Thing.objects.create(title="Test Title", subtitle="Test Subtitle", description="Test Description")

    def test_search(self):
        results = Thing.objects.search("Test")
        self.assertEqual(results.count(), 1)
