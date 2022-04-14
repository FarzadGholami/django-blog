from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse


class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='user1')
        cls.post1 = Post.objects.create(
            title='post1',
            text='this is description',
            status=Post.STATUS_CHOICES[0][0],  # published
            author=user,

        )
        cls.post2 = Post.objects.create(
            title='post2',
            text='lorem ipsum post2',
            status=Post.STATUS_CHOICES[1][0],  # draft
            author=user,
        )

  #  def setUp(self):

    def test_post_list_url(self):    # unit tests
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_url_by_name(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_title_blog(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)

    def test_post_detail_url(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url_by_name(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_blog_page(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_status_404_if_post_not_exist(self):
        response = self.client.get(reverse('post_detail', args=[555]))
        self.assertEqual(response.status_code, 404)

# django test id templates is correct

    def test_draft_post_list(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

    def test_post_model_ste(self):
        post = self.post1
        self.assertEqual(str(post), post.title)



