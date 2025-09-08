from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser

class TipoUsuario(models.Model):
    nome_tipo = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome_tipo

class Usuario(models.Model):
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=False)
    email = models.EmailField(unique=False)
    senha = models.CharField(max_length=255)
    endereco_entrega = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ano_modelo = models.IntegerField()
    quilometragem = models.IntegerField()
    potencia = models.CharField(max_length=100)
    consumo = models.CharField(max_length=100)
    historico_dono = models.TextField(blank=True, null=True)
    marca = models.CharField(max_length=100)
    foto_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.ano_modelo})"


class StatusCredito(models.Model):
    nome_status = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome_status


class Compra(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    status_credito = models.ForeignKey(StatusCredito, on_delete=models.CASCADE)

    def __str__(self):
        return f"Compra {self.id} - {self.cliente.nome}"


class Financeiro(models.Model):
    valor_cofre = models.DecimalField(max_digits=15, decimal_places=2)


class AquisicaoVeiculo(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2)
    data_aquisicao = models.DateField()



class TransacaoFinanceira(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, null=True, blank=True)
    aquisicao = models.ForeignKey(AquisicaoVeiculo, on_delete=models.CASCADE, null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_transacao = models.CharField(max_length=20)
    data_transacao = models.DateTimeField(auto_now_add=True)
