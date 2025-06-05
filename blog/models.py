import uuid
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=200)
    created_date = models.DateTimeField(
        default=timezone.now
    )
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.tag

class Question(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now
    )
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    update_date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag,  related_name='questions', through='QuestionTag')
    
    class Meta:
        ordering = ['-created_date']
        
    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.title}-{str(uuid.uuid4())[:4]}')
        super().save(*args, **kwargs)
        
    def get_top_questions():
        return Question.objects.order_by('-views')[:3]

    def get_absolute_url(self):
        return reverse('blog:question_detail', args=[self.slug])

    def __str__(self):
        return self.title
    
    
class Answer(models.Model):
    body = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    update_date = models.DateTimeField(auto_now=True)
    is_accepted = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_date']
        
    def __str__(self):
        return self.body
    
    
class QuestionTag(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('question', 'tag')

    def __str__(self):
        return f"{self.question.title} - {self.tag.tag}"