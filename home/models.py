__author__ = 'ali'

from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


class Post(models.Model):
    content = models.CharField(max_length=300)
    user = models.ForeignKey(User)
    tags = TaggableManager()
    rate_up = models.IntegerField(default=0)
    rate_down = models.IntegerField(default=0)
    rated_by = models.ManyToManyField(User, related_name='rated_posts', symmetrical=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)

    def __str__(self):
        return self.content[:30]

    class Meta:
        db_table = 'post'
        ordering = ['-created_at']

    def get_absolute_url(self):
        return '/public/'
