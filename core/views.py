from django.shortcuts import render, redirect, get_object_or_404,redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *

# Create your views here.

def carros_listar(request):
    veiculos = Veiculo.objects.all()
    context = {'veiculos': veiculos}
    return render(request, "home.html", context)

def login_fake(request):
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        if email == "vendedor@teste.com":
            request.session["tipo"] = "vendedor"
            return redirect("painel")
        else:
            request.session["tipo"] = "usuario"
            return redirect("home")

    return render(request, "login.html")

def logout_fake(request):
    request.session.flush()
    return redirect("home")

def painel_vendedor(request):
    if request.session.get("tipo") == "vendedor":
        veiculos = Veiculo.objects.all()
        return render(request, "painel.html", {"veiculos": veiculos})
    return redirect("listar")

def veiculos_listar_remover(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'removeveiculo.html', {'veiculos': veiculos})

def veiculo_remover(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    veiculo.delete()
    return redirect('home')

def veiculos_infos(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    return render(request, 'infos.html', {'veiculo': veiculo})

def veiculo_editar(request,id):
    veiculo = get_object_or_404(Veiculo,id=id)
   
    if request.method == 'POST':
        form = VeiculoForm(request.POST,request.FILES,instance=veiculo)

        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = VeiculoForm(instance=veiculo)

    return render(request,'formveiculo.html',{'form':form})

def veiculo_criar(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = VeiculoForm()
            return redirect('home')
    else:
        form = VeiculoForm()

    return render(request, "formveiculo.html", {'form': form})