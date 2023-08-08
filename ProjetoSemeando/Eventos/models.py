from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.nome

class Evento(models.Model):
    titulo = models.CharField(max_length=255)
    data = models.DateField()
    descricao = models.TextField()
    valor_entrada = models.DecimalField(max_digits=10, decimal_places=2)
    data_postagem = models.DateField(auto_now_add=True , null=True, blank=True)
    foto_principal = models.ImageField(upload_to='media/', blank=True, null=True)
    cep = models.CharField(max_length=8)
    rua = models.CharField(max_length=255, null=True, blank=True)
    numero = models.CharField(max_length=8)
    cidade = models.CharField(max_length=255, null=True, blank=True)  
    categoria = models.ForeignKey(Categoria, related_name='eventos_categoria', on_delete=models.CASCADE, null=False, blank=False)