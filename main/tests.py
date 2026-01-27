from django.test import TestCase
from django.urls import reverse


class MainPagesStatusCodeTests(TestCase):
    def test_home_page_returns_200(self):
        response = self.client.get(reverse("main:home"))
        self.assertEqual(response.status_code, 200)

    def test_about_page_returns_200(self):
        response = self.client.get(reverse("main:about"))
        self.assertEqual(response.status_code, 200)

    def test_tasks_january_page_returns_200(self):
        response = self.client.get(reverse("main:tasks_january"))
        self.assertEqual(response.status_code, 200)
