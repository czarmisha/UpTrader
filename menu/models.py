from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    url = models.CharField(max_length=255, blank=True)
    named_url = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    def get_children(self):
        return MenuItem.objects.filter(parent=self)

    def is_parent(self):
        return MenuItem.objects.filter(parent=self).exists()

    def has_children(self):
        return self.children.exists()

    def get_descendants(self):
        descendants = []
        for child in self.children.all():
            descendants.append(child)
            descendants.extend(child.get_descendants())
        return descendants

    def get_ancestors(self):
        ancestors = []
        if self.parent:
            ancestors.append(self.parent)
            ancestors.extend(self.parent.get_ancestors())
        return ancestors
