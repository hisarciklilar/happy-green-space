from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Reply


class PostModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'
            )
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            content='This is test for the post.',
            author=self.user
            )

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.slug, 'test-post')
        self.assertEqual(self.post.content, 'This is test for the post.')
        self.assertEqual(self.post.author, self.user)


class ReplyModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'
            )
        self.replier = User.objects.create_user(
            username='testreplier',
            email='testreplier@example.com',
            password='testpass123'
            )
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            content='This is test for the post.',
            author=self.user
            )
        self.reply = Reply.objects.create(
            body='This is a test reply.',
            author=self.replier,
            post=self.post
        )

    def test_reply_creation(self):
        self.assertEqual(self.reply.body, 'This is a test reply.')
        self.assertEqual(self.reply.author, self.replier)
        self.assertEqual(self.reply.post, self.post)


class PostListViewTests(TestCase):
    def test_post_list_view_status_code(self):
        response = self.client.get(reverse("forum:post_list"))
        self.assertEqual(response.status_code, 200)

    def test_post_list_view_template_used(self):
        response = self.client.get(reverse("forum:post_list"))
        self.assertTemplateUsed(response, "forum/post_list.html")
