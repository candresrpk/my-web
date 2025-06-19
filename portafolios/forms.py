from django import forms
from .models import Project, ProjectTag, Tag

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'tags', 'image', 'git_url']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].queryset = Tag.objects.all()
        
    def save(self, commit=True):
        project = super().save(commit=False)
        tags = self.cleaned_data['tags']
        if commit:
            project.save()
            for tag in tags:
                ProjectTag.objects.create(project=project, tag=tag)
        return project
        
    def clean_tags(self):
        tags = self.cleaned_data['tags']
        if len(tags) > 5:
            raise forms.ValidationError("No puedes seleccionar más de 5 etiquetas.")
        return tags
    
    def clean(self):
        cleaned_data = super().clean()
        tags = cleaned_data.get('tags')
        if not tags:
            raise forms.ValidationError("Debes seleccionar al menos una etiqueta.")
        return cleaned_data
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if Project.objects.filter(title=title).exists():
            raise forms.ValidationError("Ya existe un proyecto con el mismo título.")
        return title
    
    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 20:
            raise forms.ValidationError("La descripción debe tener al menos 20 caracteres.")
        return description
    
    
    def clean_git_url(self):
        git_url = self.cleaned_data['git_url']
        if git_url and not git_url.startswith('https://github.com/'):
            raise forms.ValidationError("La URL debe comenzar con 'https://github.com/'.")
        return git_url
    

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        
    def clean_tag(self):
        tag = self.cleaned_data['name']
        if Tag.objects.filter(tag=tag).exists():
            raise forms.ValidationError("Ya existe una etiqueta con el mismo nombre.")
        return tag
    
    def save(self, commit=True):
        tag = super().save(commit=False)
        if commit:
            tag.save()
        return tag
    
        
class ProjectTagForm(forms.ModelForm):
    class Meta:
        model = ProjectTag
        fields = ['tag']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tag'].queryset = Tag.objects.all()
        
    def save(self, commit=True):
        project_tag = super().save(commit=False)
        if commit:
            project_tag.save()
        return project_tag
    
    