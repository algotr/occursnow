__author__ = 'ali'

from django import template


register = template.Library()


@register.filter
def total_rating(post):
    return post.rate_up - post.rate_down
