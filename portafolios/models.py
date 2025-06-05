import uuid
from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='portafolio/images')
    git_url = models.URLField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.title}-{str(uuid.uuid4())[:4]}')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/portafolio/{self.slug}'
    
    def get_tags(self):
        return ', '.join([tag.name for tag in self.tags.all()])
    
    
    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
            

class ProjectTag(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('project', 'tag')
        verbose_name = 'Etiqueta de Proyecto'
        verbose_name_plural = 'Etiquetas de Proyectos'
        
    def __str__(self):
        return f"{self.project} - {self.tag}"
    

