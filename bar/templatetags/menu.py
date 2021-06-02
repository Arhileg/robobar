from django import template

register = template.Library()

@register.inclusion_tag('menu_item.html', takes_context=True)
def menu_item(context, url_name, title):
    return {
        'request': context['request'], 'url_name': url_name, 'title': title
    }
