from django import template
register = template.Library()


@register.inclusion_tag("tags/email_status_tag.html", takes_context=True)
def email_status(context):
    email = context
    return {
        "email_status": email
    }

