from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

from .managers import PublisheManager


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
    published = PublisheManager()

    class Meta:
        ordering = ['-publish', ]

    def get_absolute_url(self, *args, **kwargs):
        return reverse('blogs:post-detail', args=[str(self.pk)])

    def __str__(self):
        return self.title
