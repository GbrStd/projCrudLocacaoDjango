from django.shortcuts import render, redirect

from locacao.forms import LocacaoForm
from locacao.models import Locacao


# Create your views here.

def list_locacao(request):
    locacao = Locacao.objects.all()
    return render(request, 'locacao.html', {'locacao': locacao})


def create_locacao(request):
    form = LocacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_locacao')

    return render(request, 'locacao-form.html', {'form': form})


def update_locacao(request, id):
    locacao = Locacao.objects.get(id=id)
    form = LocacaoForm(request.POST or None, instance=locacao)

    if form.is_valid():
        form.save()
        return redirect('list_locacao')

    return render(request, 'locacao-form.html', {'form': form, 'locacao': locacao})


def delete_locacao(request, id):
    locacao = Locacao.objects.get(id=id)

    if request.method == 'POST':
        locacao.delete()
        return redirect('list_locacao')

    return render(request, 'locacao-delete-confirm.html', {'locacao': locacao})
