from django.shortcuts import render
from rest_framework import serializers
from rest_framework import viewsets
from Eventos.models import Evento, Categoria
from rest_framework import filters
from django.db.models import Q

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        # campos que queremos serializar
        fields = ('id', 'nome')

class EventoSerializer(serializers.ModelSerializer):
    foto_principal = serializers.ImageField(max_length=None, use_url=True, required=False)

    categoria = serializers.SlugRelatedField(
        queryset=Categoria.objects.all(),
        slug_field='nome'  
    )
    class Meta:
        model = Evento
        # campos que queremos serializar
        fields = ('id', 'user','titulo', 'data','descricao','valor_entrada','data_postagem',
                   'foto_principal','categoria','cep','rua','numero','cidade')

class CategoriaView(viewsets.ModelViewSet):
    queryset = Categoria.objects.all() 
    serializer_class = CategoriaSerializer  
    http_method_names = ['get', 'post', 'put', 'delete']

class EventoView(viewsets.ModelViewSet):
    queryset = Evento.objects.all() 
    serializer_class = EventoSerializer  
    http_method_names = ['get', 'post', 'put', 'delete']
    def perform_create(self, serializer):
        # Automatically associate the user with the event
        serializer.save(user=self.request.user)

    # filter_backends = [filters.SearchFilter]  # Enable search filtering
    # search_fields = ['titulo', 'descricao', 'categoria__nome']

    # def get_queryset(self):
    #     queryset = Evento.objects.all()

    #     letter_filter = self.request.query_params.get('letter', None)
    #     if letter_filter:
    #         queryset = queryset.filter(titulo__istartswith=letter_filter)

    #     return queryset