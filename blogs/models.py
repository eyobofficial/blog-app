from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

from .managers import PublishedManager, CommentManager


class Post(models.Model):
    """
    Abstracts a blog post
    """
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique_for_date='publish')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft',
    )

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish', ]

    def get_absolute_url(self, *args, **kwargs):
        return reverse('blogs:post-detail', args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug
        ])

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField('Full Name', max_length=60)
    email = models.EmailField()
    body = models.TextField('Comment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=True)

    # Managers
    objects = CommentManager()

    class Meta:
        ordering = ['created_at', ]

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
