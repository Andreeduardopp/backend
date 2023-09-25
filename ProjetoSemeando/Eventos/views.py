from django.shortcuts import render
from rest_framework import serializers, viewsets, status, filters
from Eventos.models import Evento, Categoria
from datetime import date, timedelta, timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS
from Usuarios.models import User
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action


class OrganizadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name")


class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 100


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        # campos que queremos serializar
        fields = ("id", "nome")


class EventoReadSerializer(serializers.ModelSerializer):
    hora_inicio = serializers.TimeField(format="%H:%M")
    foto_principal = serializers.ImageField(
        max_length=None, use_url=True, required=False
    )
    user = OrganizadorSerializer(read_only=True)
    categoria = serializers.SlugRelatedField(
        queryset=Categoria.objects.all(), slug_field="nome"
    )

    class Meta:
        model = Evento
        # campos que queremos serializar
        fields = (
            "id",
            "user",
            "titulo",
            "data",
            "hora_inicio",
            "descricao",
            "valor_entrada",
            "data_postagem",
            "foto_principal",
            "categoria",
            "cep",
            "rua",
            "numero",
            "cidade",
        )

  


class EventowriteSerializer(serializers.ModelSerializer):
    foto_principal = serializers.ImageField(
        max_length=None, use_url=True, required=False
    )
    categoria = serializers.SlugRelatedField(
        queryset=Categoria.objects.all(), slug_field="nome"
    )

    class Meta:
        model = Evento
        # campos que queremos serializar
        fields = (
            "id",
            "user",
            "titulo",
            "data",
            "hora_inicio",
            "descricao",
            "valor_entrada",
            "data_postagem",
            "foto_principal",
            "categoria",
            "cep",
            "rua",
            "numero",
            "cidade",
        )


class CategoriaView(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    http_method_names = ["get", "post", "put", "delete"]


class EventoView(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoReadSerializer
    http_method_names = ["get", "post", "put", "delete"]
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    search_fields = ["titulo", "descricao"]
    pagination_class = CustomPagination
    ordering_fields = ["data"]
    ordering = ["data"]

    def delete_old_events(self):
        current_date =  date.today()
        deleted_count, _ = Evento.objects.filter(data__lt=current_date).delete()
        return deleted_count

    @action(detail=False, methods=["get"])
    def get_events_by_user(self, request):
    
        user_id = request.query_params.get("user_id")
        events = Evento.objects.filter(user__id=user_id)
        serializer = EventoReadSerializer(events, many=True)
        data = serializer.data
        for event in data:
            if event["foto_principal"]:
                event["foto_principal"] = request.build_absolute_uri(event["foto_principal"])

        return Response(data=data)
    
    
    def get_queryset(self):
        self.delete_old_events()
        current_date = date.today()

        # Filtrar os eventos com datas maiores ou iguais à data atual
        return Evento.objects.filter(data__gte=current_date)

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return super().get_serializer_class()
        return EventowriteSerializer


class EventosDaSemanaView(viewsets.ModelViewSet):
    serializer_class = EventoReadSerializer
    http_method_names = ["get", "post", "put", "delete"]
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    search_fields = ["titulo", "descricao"]
    pagination_class = CustomPagination
    ordering_fields = ["data"]
    ordering = ["data"]

    def get_queryset(self):
        current_date = date.today()
        inicio_semana = current_date
        fim_semana = inicio_semana + timedelta(days=6)
        return Evento.objects.filter(data__range=[inicio_semana, fim_semana])
