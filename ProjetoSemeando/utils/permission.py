from rest_framework.permissions import DjangoModelPermissions


class CustomDjangoModelPermissions(DjangoModelPermissions):
    def has_permission(self, request, view):
        # Verifica o método da solicitação
        if request.method in ['POST', 'PUT']:
            # Se o método for POST ou PUT, exige autenticação
            return request.user and request.user.is_authenticated
        # Para outros métodos, como GET, permite o acesso sem autenticação
        return True