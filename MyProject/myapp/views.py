from django.shortcuts import redirect, render
from myapp.models import  *
from myapp.forms import *
from django.contrib import messages

# Create your views here.

def usuario(request):
    return render(request, 'myapp/usuario.html',{"itens": Product.objects.all()})

def index(request):
    return render(request, 'myapp/index.html',{"itens": Product.objects.all()})

def cadastrar(request):
    form = ItensProduct
    if request.method == "POST":
        form = ItensProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'item cadastrada com sucesso!')
            return redirect('index')
        
    return render(request, "myapp/create.html", {"forms":form})

def editar(request, id):
    item = Product.objects.get(pk=id)
    form = ItensProduct(instance=item)
    return render(request, "myapp/update.html",{"form":form, "item":item})


def atualizar(request, id):
    try:
        if request.method == "POST":
            item = Product.objects.get(pk=id)
            form = ItensProduct(request.POST, request.FILES, instance=item)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'item foi alterada com sucesso!')
                return redirect('index')
    except Exception as e:
        messages.error(request, e)
        return redirect('index')
            

def visualizar(request, id):
    item = Product.objects.get(pk=id)
    return render(request, "myapp/read.html", {"item":item})

def deletar(request, id):
    item = Product.objects.get(pk=id)
    item.delete()
    messages.success(request, 'item foi deletada com sucesso!')
    return redirect('index')