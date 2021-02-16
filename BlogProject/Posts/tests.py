from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


# Create your tests here.

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser = User.objects.create_user(username='bhanu1', password='bhanu1')
        testuser.save()

        test_post = Post.objects.create(
            author=testuser, title='Blog title', body='Body content',
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'bhanu1')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, 'Body content')
