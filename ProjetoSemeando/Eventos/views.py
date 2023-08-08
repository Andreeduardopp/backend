from django.shortcuts import render
from rest_framework import serializers
from rest_framework import viewsets
from Eventos.models import Evento, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        # campos que queremos serializar
        fields = ('id', 'nome')

class EventoSerializer(serializers.ModelSerializer):
    foto_principal = serializers.ImageField(max_length=None, use_url=True, required=False)
    class Meta:
        model = Evento
        # campos que queremos serializar
        fields = ('id', 'titulo', 'data','descricao','valor_entrada','data_postagem',
                   'foto_principal','categoria','cep','rua','numero','cidade')

class CategoriaView(viewsets.ModelViewSet):
    queryset = Categoria.objects.all() 
    serializer_class = CategoriaSerializer  
    http_method_names = ['get', 'post', 'put', 'delete']

class EventoView(viewsets.ModelViewSet):
    queryset = Evento.objects.all() 
    serializer_class = EventoSerializer  
    http_method_names = ['get', 'post', 'put', 'delete'] 