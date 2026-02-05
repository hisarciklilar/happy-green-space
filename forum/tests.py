from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Post, Reply


class ForumTestBase(TestCase):
    """Setup base test data for forum tests: two users, one post, one reply."""

    def setUp(self):
        self.client = Client()

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

    def login(self, user):
        self.client.login(username=user.username, password='testpass123')


class PostModelTests(ForumTestBase):
    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.slug, 'test-post')
        self.assertEqual(self.post.content, 'This is test for the post.')
        self.assertEqual(self.post.author, self.user)


class ReplyModelTests(ForumTestBase):        
    def test_reply_creation(self):
        self.assertEqual(self.reply.body, 'This is a test reply.')
        self.assertEqual(self.reply.author, self.replier)
        self.assertEqual(self.reply.post, self.post)


class PostListViewTests(ForumTestBase):
    def test_post_list_view_status_code(self):
        response = self.client.get(reverse("forum:post_list"))
        self.assertEqual(response.status_code, 200)

    def test_post_list_view_template_used(self):
        response = self.client.get(reverse("forum:post_list"))
        self.assertTemplateUsed(response, "forum/post_list.html")

    def test_contains_existing_post_title(self):
        response = self.client.get(reverse("forum:post_list"))
        self.assertContains(response, self.post.title)


class PostDetailViewTests(ForumTestBase):
    def test_post_detail_view_status_code(self):
        response = self.client.get(reverse("forum:post_detail", 
                                           kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view_template_used(self):
        response = self.client.get(reverse("forum:post_detail", 
                                           kwargs={'slug': self.post.slug}))
        self.assertTemplateUsed(response, "forum/post_detail.html")

    def test_contains_existing_post_content(self):
        response = self.client.get(reverse("forum:post_detail", 
                                           kwargs={'slug': self.post.slug}))
        self.assertContains(response, self.post.content)

    def test_contains_existing_reply_body(self):
        response = self.client.get(reverse("forum:post_detail", 
                                           kwargs={'slug': self.post.slug}))
        self.assertContains(response, self.reply.body)

    def test_returns_404_for_bad_slug(self):
        response = self.client.get(reverse("forum:post_detail", 
                                           kwargs={'slug': 'nonexistent-slug'}))
        self.assertEqual(response.status_code, 404)


class PostCreateViewTests(ForumTestBase):
    def test_post_create_view_redirects_if_not_logged_in(self):
        response = self.client.get(reverse("forum:post_create"))
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.url)

    def test_logged_in_gets_200(self):
        self.login(self.user)
        response = self.client.get(reverse("forum:post_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "forum/post_form.html")

    def test_post_creation_via_view(self):
        self.login(self.user)
        response = self.client.post(reverse("forum:post_create"), {
            'title': 'New Test Post',
            'content': 'Content for the new test post.'
        })
        self.assertEqual(response.status_code, 302)
        new_post = Post.objects.get(title='New Test Post')
        self.assertEqual(new_post.content, 'Content for the new test post.')
        self.assertEqual(new_post.author, self.user)
        self.assertEqual(new_post.slug, 'new-test-post')

    def test_post_creation_with_duplicate_title(self):
        self.login(self.user)
        response1 = self.client.post(reverse("forum:post_create"), {
            'title': 'Duplicate Title',
            'content': 'First post content.'
        })
        response2 = self.client.post(reverse("forum:post_create"), {
            'title': 'Duplicate Title',
            'content': 'Second post content.'
        })
        post1 = Post.objects.get(title='Duplicate Title', content='First post content.')
        post2 = Post.objects.get(title='Duplicate Title', content='Second post content.')
        self.assertEqual(post1.slug, 'duplicate-title')
        self.assertEqual(post2.slug, 'duplicate-title-2')


class PostUpdateViewTests(ForumTestBase):
    def test_post_update_view_redirects_if_not_logged_in(self):
        response = self.client.get(reverse("forum:post_update", kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.url)

    def test_non_author_gets_404(self):
        self.login(self.replier)
        response = self.client.get(reverse("forum:post_update", kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 404)
  
    def test_post_update_view_gets_200_for_author(self):
        self.login(self.user)
        response = self.client.get(reverse("forum:post_update", kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "forum/post_form.html")

    def test_post_update_via_view(self):
        self.login(self.user)
        response = self.client.post(reverse("forum:post_update", kwargs={'slug': self.post.slug}), {
            'title': 'Updated Test Post',
            'content': 'Updated content for the test post.'
        })
        updated_post = Post.objects.get(pk=self.post.pk)
        self.assertEqual(updated_post.title, 'Updated Test Post')
        self.assertEqual(updated_post.content, 'Updated content for the test post.')
        self.assertEqual(updated_post.author, self.user)
        self.assertEqual(updated_post.slug, 'updated-test-post')


class PostDeleteViewTests(ForumTestBase):
    def test_post_delete_view_redirects_if_not_logged_in(self):
        response = self.client.get(reverse("forum:post_delete", kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.url)

    def test_non_author_gets_404(self):
        self.login(self.replier)
        response = self.client.get(reverse("forum:post_delete", kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 404)
    
    def test_post_delete_view_gets_200_for_author(self):
        self.login(self.user)
        response = self.client.get(reverse("forum:post_delete", kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "forum/post_confirm_delete.html")

    def test_delete_removes_post(self):
        self.login(self.user)
        self.client.post(reverse("forum:post_delete", kwargs={'slug': self.post.slug}))
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())

    def test_delete_redirects_to_post_list(self):   
        self.login(self.user)
        response = self.client.post(reverse("forum:post_delete", kwargs={'slug': self.post.slug}))
        self.assertEqual(response.url, reverse("forum:post_list"))


class ReplyCreateViewTests(ForumTestBase):
    def test_reply_create_view_redirects_if_not_logged_in(self):
        response = self.client.get(reverse("forum:reply_create", kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.url)

    def test_logged_in_gets_200(self):
        self.login(self.replier)
        response = self.client.get(reverse("forum:reply_create", kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "forum/reply_form.html")

    def test_logged_in_user_can_create_reply(self):
        self.login(self.replier)
        response = self.client.post(reverse("forum:reply_create", kwargs={'slug': self.post.slug}), {
            'body': 'This is another test reply.'
        })
        self.assertEqual(response.status_code, 302)
        new_reply = Reply.objects.get(body='This is another test reply.')
        self.assertEqual(new_reply.author, self.replier)
        self.assertEqual(new_reply.post, self.post)

    def test_create_reply_redisrects_to_post_detail(self):
        self.login(self.replier)
        response = self.client.post(reverse("forum:reply_create", kwargs={'slug': self.post.slug}), {
            'body': 'This is another test reply.'
        })
        self.assertEqual(response.url, reverse("forum:post_detail", kwargs={'slug': self.post.slug}))


class ReplyUpdateViewTests(ForumTestBase):
    def test_anonymous_user_redirected(self):
        response = self.client.get(reverse("forum:reply_update", kwargs={'pk': self.reply.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.url)
   
    def test_non_author_gets_404(self):
        self.login(self.user)
        response = self.client.get(reverse("forum:reply_update", kwargs={'pk': self.reply.pk}))
        self.assertEqual(response.status_code, 404)
   
    def test_author_gets_200(self):
        self.login(self.replier)
        response = self.client.get(reverse("forum:reply_update", kwargs={'pk': self.reply.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "forum/reply_form.html")

    def test_update_redirects_to_post_detail(self):
        self.login(self.replier)
        response = self.client.post(reverse("forum:reply_update", kwargs={'pk': self.reply.pk}), {
            'body': 'Updated reply body.'
        })
        self.assertEqual(response.url, reverse("forum:post_detail", kwargs={'slug': self.post.slug}))


class ReplyDeleteViewTests(ForumTestBase):
    def test_anonymous_user_redirected(self):
        response = self.client.get(reverse("forum:reply_delete", kwargs={'pk': self.reply.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.url)
   
    def test_non_author_gets_404(self):
        self.login(self.user)
        response = self.client.get(reverse("forum:reply_delete", kwargs={'pk': self.reply.pk}))
        self.assertEqual(response.status_code, 404)
   
    def test_author_gets_200(self):
        self.login(self.replier)
        response = self.client.get(reverse("forum:reply_delete", kwargs={'pk': self.reply.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "forum/reply_confirm_delete.html")

    def test_delete_removes_reply(self):
        self.login(self.replier)
        self.client.post(reverse("forum:reply_delete", kwargs={'pk': self.reply.pk}))
        self.assertFalse(Reply.objects.filter(pk=self.reply.pk).exists())

    def test_delete_redirects_to_post_detail(self):   
        self.login(self.replier)
        response = self.client.post(reverse("forum:reply_delete", kwargs={'pk': self.reply.pk}))
        self.assertEqual(response.url, reverse("forum:post_detail", kwargs={'slug': self.post.slug}))
