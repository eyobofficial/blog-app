from django.db import models


class PublishedManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class CommentManager(models.Manager):

    def approved(self, *args, **kwargs):
        return self.model.objects.filter(is_approved=True)