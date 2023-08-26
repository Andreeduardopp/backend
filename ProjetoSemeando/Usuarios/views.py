from rest_framework import serializers
from rest_framework import viewsets
from Usuarios.models import User
from rest_framework.permissions import SAFE_METHODS

class UserWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'is_staff','is_active','date_joined','user_permissions','groups','last_login']

class UserReadSerializer(serializers.ModelSerializer):
    groups = serializers.SerializerMethodField()
    user_permissions = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'is_staff']

    def get_groups(self, instance):
        group_names = []
        for group in instance.groups.all():
            group_names.append(group.name)
        return group_names
    
    def get_user_permissions(self, instance):
        # percorremos todas as permissões da instância e montamos uma lista com os nomes para retornar no lugar dos códigos
        perms_names = []
        for perm in instance.user_permissions.all():
            perms_names.append(perm.codename)
        return perms_names


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all() 
    serializer_class = UserReadSerializer
    http_method_names = ['get', 'put', 'delete']  

    # sobre escrevemos o get_serializer_class para poder alternar entre read e write
    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return super().get_serializer_class()
        return UserWriteSerializer