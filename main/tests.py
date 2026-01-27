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


class MainTemplateUsedTests(TestCase):
    def test_home_page_uses_correct_template(self):
        response = self.client.get(reverse("main:home"))
        self.assertTemplateUsed(response, "main/home.html")

    def test_about_page_uses_correct_template(self):
        response = self.client.get(reverse("main:about"))
        self.assertTemplateUsed(response, "main/about.html")

    def test_tasks_january_page_uses_correct_template(self):
        response = self.client.get(reverse("main:tasks_january"))
        self.assertTemplateUsed(response, "main/tasks_january.html")


class MainUrlAccessibleTests(TestCase):
    def test_home_page_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_about_page_url(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_tasks_january_page_url(self):
        response = self.client.get("/tasks_january/")
        self.assertEqual(response.status_code, 200)


class MainUrlResolvesTests(TestCase):
    def test_home_page_resolves(self):
        url = reverse("main:home")
        self.assertEqual(url, "/")

    def test_about_page_resolves(self):
        url = reverse("main:about")
        self.assertEqual(url, "/about/")

    def test_tasks_january_page_resolves(self):
        url = reverse("main:tasks_january")
        self.assertEqual(url, "/tasks_january/")
