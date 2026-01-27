from django.test import TestCase
from django.urls import reverse

class PostListViewTests(TestCase):
    def test_post_list_view_status_code(self):
        response = self.client.get(reverse("forum:post_list"))
        self.assertEqual(response.status_code, 200)

    def test_post_list_view_template_used(self):
        response = self.client.get(reverse("forum:post_list"))
        self.assertTemplateUsed(response, "forum/post_list.html")
