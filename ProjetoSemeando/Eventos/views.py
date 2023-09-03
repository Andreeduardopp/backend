from django.shortcuts import render
from rest_framework import serializers
from rest_framework import viewsets
from Eventos.models import Evento, Categoria
from rest_framework import filters
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        # campos que queremos serializar
        fields = ('id', 'nome')

class EventoSerializer(serializers.ModelSerializer):
    foto_principal = serializers.ImageField(max_length=None, use_url=True, required=False)
    user = serializers.CharField(source='user.username', read_only=True)
    categoria = serializers.SlugRelatedField(
        queryset=Categoria.objects.all(),
        slug_field='nome'  
    )
    class Meta:
        model = Evento
        # campos que queremos serializar
        fields = ('id', 'user','titulo', 'data','hora_inicio','descricao','valor_entrada','data_postagem',
                   'foto_principal','categoria','cep','rua','numero','cidade')

class CategoriaView(viewsets.ModelViewSet):
    queryset = Categoria.objects.all() 
    serializer_class = CategoriaSerializer  
    http_method_names = ['get', 'post', 'put', 'delete']

class EventoView(viewsets.ModelViewSet):
    queryset = Evento.objects.all() 
    serializer_class = EventoSerializer  
    http_method_names = ['get', 'post', 'put', 'delete']
    filter_backends = [filters.SearchFilter, DjangoFilterBackend,filters.OrderingFilter]  
    search_fields = ['titulo', 'descricao']

