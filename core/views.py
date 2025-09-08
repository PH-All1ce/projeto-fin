from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def carros_listar(request):
    veiculos = Veiculo.objects.all()
    context = {'veiculos': veiculos}
    return render(request, "home.html", context)

def login_fake(request):
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")  # só pra simular, não valida

        if email == "vendedor@teste.com":
            request.session["tipo"] = "vendedor"
            return redirect("painel")
        else:
            request.session["tipo"] = "usuario"
            return redirect("home")

    return render(request, "login.html")

def logout_fake(request):
    request.session.flush()  # limpa a sessão
    return redirect("home")

def painel_vendedor(request):
    if request.session.get("tipo") == "vendedor":
        return render(request, "painel.html")
    return redirect("listar")