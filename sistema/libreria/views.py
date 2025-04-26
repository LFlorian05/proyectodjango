from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .forms import LibroForm
from django.contrib.auth.decorators import login_required


@login_required

def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'paginas/listar_libros.html', {'libros': libros})

@login_required

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:  
        form = LibroForm()
    return render(request, 'paginas/crear_libro.html', {'form': form})

@login_required

def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'paginas/editar_libro.html', {'form': form})

@login_required

def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        libro.delete()
        return redirect('listar_libros')
    return render(request, 'paginas/eliminar_libro.html', {'libro': libro})
