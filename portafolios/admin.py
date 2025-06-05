from django.contrib import admin
from .models import Project, ProjectTag, Tag

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectTag)
admin.site.register(Tag)