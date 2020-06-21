from django import template
from django.contrib.auth.models import Group

register = template.Library()

# Custom made filter to check in the templates if a user is in a specific group
@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False
