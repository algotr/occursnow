__author__ = 'ali'

from accounts.forms import LoginForm, RegisterForm
from django import template


register = template.Library()


@register.inclusion_tag('includes/login_register.html')
def login_register_forms():
    # cache or get cached version of pages
    return {'login_form': LoginForm(), 'register_form': RegisterForm()}
