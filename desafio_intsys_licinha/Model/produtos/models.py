from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Produtos(models.Model):
    id = models.IntegerField("id", primary_key = True)
    nome = models.CharField("Nome do produto", max_length = 50)
    quantidade = models.CharField("Unidades (apenas dígitos)", max_length = 3, validators=[RegexValidator(r'^\d{1,10}$')]) # Só pode digitar números
    cidade = models.CharField("Cidade", max_length = 40)
    rua = models.CharField("Endereço (Rua/Bairro)", max_length = 100)
    agendamento = models.DateField("Data de coleta")
    nome_de_usuario = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ("cidade",)
        verbose_name_plural = 'Produtos'