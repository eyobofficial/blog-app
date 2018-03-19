from django.db import models


class PublishManage(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super(PublishManage, self).get_queryset().filter(status='published')