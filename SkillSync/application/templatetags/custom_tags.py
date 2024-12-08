from django import template

register = template.Library()

@register.inclusion_tag("recursivetree.html")
def renderNestedDict(jsonData):
    if not isinstance(jsonData, dict):
        return {"jsonData": {}}
    return {"jsonData": jsonData}

@register.filter(name="is_dict")
def is_dict(value):
    return isinstance(value, dict)