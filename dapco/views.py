from django.shortcuts import render, redirect
from .models import Encuesta, Pregunta, Opcion, Respuesta, Distribucion, Usuario
from .forms import EncuestaForm
# Create your views here.


def index(request):
    
    context = {
        'encuestas': Encuesta.objects.all(),
    }
    
    return render(request, 'dapco/index.html', context)


def createEncuestView(request):
    
    if request.method == 'POST':
        form = EncuestaForm(request.POST)
        if form.is_valid():
            encuesta = form.save(commit=False)
            encuesta.owner = request.user
            encuesta.save()
            return redirect('dapco:index')
    else:
        form = EncuestaForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'dapco/create.html', context)