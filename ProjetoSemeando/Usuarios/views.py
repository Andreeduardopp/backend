from rest_framework import serializers
from rest_framework import viewsets
from Usuarios.models import User
from rest_framework.permissions import SAFE_METHODS

class UserWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'is_staff','is_active','date_joined','user_permissions','groups','last_login']

class UserReadSerializer(serializers.ModelSerializer):
    # eventos = EventoSerializer(many=True, read_only=True, source='eventos_set')
    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'is_staff','is_active','user_permissions','groups',]



class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all() 
    serializer_class = UserReadSerializer
    http_method_names = ['get', 'put', 'delete']  

    # sobre escrevemos o get_serializer_class para poder alternar entre read e write
    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return super().get_serializer_class()
        return UserWriteSerializer