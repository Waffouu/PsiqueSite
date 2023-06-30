from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Comentario
from .forms import ComentForm
from django.forms import ModelForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ComentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('comentarios')
    else:
        form = ComentForm()

    comentarios = Comentario.objects.all()

    context = {
        'form': form,
        'comentarios': comentarios
    }

    return render(request, './site/index.html', context)

def comentarios(request):
    comentarios_validados = Comentario.objects.filter(lido=True)

    if request.method == 'POST':
        form = ComentForm(request.POST)
        if form.is_valid():
            comentarios = form.save(commit=False)
            comentarios.status = 'pendente'
            comentarios.save()

    else:
        form = ComentForm()

    context = {
        'form': form,
        'comentarios': comentarios_validados
    }

    return render(request, 'site/index.html', context)
