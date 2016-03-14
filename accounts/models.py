__author__ = 'ali'

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from occursnow import settings


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)

    def gravatar_url(self):
        return settings.STATIC_URL + "img/user.png"
        # return "http://www.gravatar.com/avatar/%s?s=50" % hashlib.md5(self.user.email.encode()).hexdigest()

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        db_table = 'user_profile'


@receiver(post_save, sender=User)
def handle_user_save(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
