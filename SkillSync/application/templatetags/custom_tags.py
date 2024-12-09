from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def renderNestedDict(data):
    """
    Recursively renders all 'title' keys in a nested dictionary
    as a properly structured HTML list with buttons.
    """

    def render_dict(d):
        html = ""
        if "title" in d:  # Render the current title
            html += f"<li><button>{d['title']}</button>"
        nested_html = ""
        # Recursively process nested dictionaries
        for key, value in d.items():
            if isinstance(value, dict):
                nested_html += render_dict(value)
        if nested_html:  # Wrap nested content in a <ul>
            html += f"<ul>{nested_html}</ul>"
        if "title" in d:  # Close the current list item only after handling children
            html += "</li>"
        return html

    # Generate the HTML structure and mark it as safe
    return mark_safe(f"<ul>{render_dict(data)}</ul>")

