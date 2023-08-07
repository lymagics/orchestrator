from django.test import SimpleTestCase
from django.urls import reverse


class TestPingViews(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = reverse('ping:ping')

    def test_ping_view_returning_pong(self):
        response =  self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'pong')
