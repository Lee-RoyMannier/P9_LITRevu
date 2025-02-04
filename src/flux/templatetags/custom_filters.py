from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def posted_by_display(context, user):
    if context["user"] == user:
        return "vous avez"
    return f"{user.username} a "
