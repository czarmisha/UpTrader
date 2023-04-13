from django import template

from menu.models import MenuItem


register = template.Library()

def draw_menu(parser, token):
    try:
        tokens = token.split_contents()
        tag_name = tokens[0]
        menu_name = tokens[1]
    except IndexError:
        raise template.TemplateSyntaxError(f"{tag_name} tag requires at least one argument")

    return MenuNode(menu_name)


class MenuNode(template.Node):
    def __init__(self, menu_name):
        self.menu_name = menu_name

    def render(self, context):
        try:
            active_item_url = context['request'].path
            menu_items = MenuItem.objects.filter(name=self.menu_name).select_related('parent')
            context['menu_items'] = menu_items
            context['active_item_url'] = active_item_url
            return template.loader.render_to_string('menu/menu.html', context.flatten())
        except template.VariableDoesNotExist:
            return ''
        except MenuItem.DoesNotExist:
            return ''
        
    def get_children(self, items):
        for item in items:
            item.children = item.menuitem_set.all()
            if item.children:
                item.children = self.get_children(item.children)
        return items

register.tag('draw_menu', draw_menu)
