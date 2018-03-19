from django.test import TestCase
from django.contrib.auth.models import User
from blogs.models import Post


def create_published_post(title, slug, author, body, ):
    return Post.objects.create(
        title=title,
        slug=slug,
        author=author,
        body=body,
        status='published'
    )


class PostViewTests(TestCase):

    def setUp(self):
        User.objects.create_user(
            'testuser',
            'testuser@test.com',
            'testuserpassword'
        )
