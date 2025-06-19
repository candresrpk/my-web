from django.shortcuts import render, redirect
from .models import Project, ProjectTag, Tag
from .forms import ProjectForm
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


def createView(request):
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            tags = form.cleaned_data['tags']
            for tag in tags:
                ProjectTag.objects.get_or_create(project=project, tag=tag)
            return redirect('portafolios:index')
    else:
        form = ProjectForm()
    
    context = {
        'form': form
        
    }
    
    
    return render(request, 'portafolios/create.html', context)