from django.test import TestCase
from blogs.models import Post
from django.contrib.auth.models import User


def create_published_post(title, slug, author, body, ):
    return Post.objects.create(
        title=title,
        slug=slug,
        author=author,
        body=body,
        status='published'
    )


class PostModelTests(TestCase):

    def setUp(self):
        User.objects.create_user(
            'testuser',
            'testuser@test.com',
            'testuserpassword'
        )

    def test_published_post_status(self):
        test_user = User.objects.get(username='testuser')
        published_post = create_published_post(
            'Published Post',
            'published-post',
            test_user,
            'Test published post text body'
        )
        self.assertEqual(published_post.status, 'published')