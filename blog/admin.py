from django.contrib import admin
from .models import Question, Answer, Tag, QuestionTag

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_date')
    prepopulated_fields = {'slug': ('title',)}  # Opcional si deseas autollenar
    search_fields = ('title', 'body')
    list_filter = ('created_date', 'author')
    ordering = ('-created_date',)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'author', 'is_accepted', 'created_date')
    list_filter = ('is_accepted', 'created_date')
    search_fields = ('body',)
    ordering = ('-created_date',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)
    search_fields = ('tag',)
    ordering = ('tag',)

@admin.register(QuestionTag)
class QuestionTagAdmin(admin.ModelAdmin):
    list_display = ('question', 'tag')
    search_fields = ('question__title', 'tag__name')
