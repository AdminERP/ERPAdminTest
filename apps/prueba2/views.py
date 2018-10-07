from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from apps.prueba2.forms import RegistrarCargoForm
from apps.prueba2.models import Job


def inicio(request):
    return render(request, 'base.html', {})


def registrar_cargo(request, id=None):
    cargo = None
    if id:
        cargo = get_object_or_404(Job, id=id)

    form = RegistrarCargoForm(instance=cargo)

    if request.method == "POST":
        form = RegistrarCargoForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect('consultar_cargo')
    return render(request, 'registrar_cargo.html', {'form': form})




def consultar_cargo(request):
    return render(request, 'consulta_cargos.html', {'lista_cargos': Job.objects.all()})