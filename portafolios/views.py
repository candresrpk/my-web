from django.shortcuts import render
from .models import Project, ProjectTag, Tag
# Create your views here.

def index(request):
        
    tag_name = request.GET.get('tag')
    tags = Tag.objects.all()
    
    if tag_name:
        projects = Project.objects.filter(tags__name=tag_name).distinct()
    else:
        projects = Project.objects.all()
    
    context = {
        'projects': projects,
        'tags': tags
    }
    
    return render(request, 'portafolios/index.html', context=context)