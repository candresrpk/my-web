from django.contrib import admin
from .models import Project, ProjectTag, Tag

# Register your models here.
admin.site.register(Tag)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('tags',)
    search_fields = ('title', 'description')
    ordering = ('-created_date',)
    list_per_page = 10

@admin.register(ProjectTag)
class ProjectTagAdmin(admin.ModelAdmin):
    search_fields = ('project__title', 'tag__name')
    list_filter = ('project', 'tag')
    ordering = ('project', 'tag')
    list_per_page = 10
    
