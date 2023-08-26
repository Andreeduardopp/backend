from django.urls import path, include
from rest_framework import routers

from Usuarios.views import UserView


router = routers.DefaultRouter()
router.register('usuarios', UserView)  

urlpatterns = [
    path('usuarios/', include(router.urls)),
]