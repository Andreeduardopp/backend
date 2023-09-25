from django.urls import path, include
from rest_framework import routers

from Eventos.views import EventoView,CategoriaView,EventosDaSemanaView


router = routers.DefaultRouter()
router.register('eventos', EventoView)  # nome do objeto da view
router.register('categorias', CategoriaView)  # nome do objeto da view
router.register('eventos-da-semana', EventosDaSemanaView, basename='eventos-da-semana')

urlpatterns = [
    path('eventos/', include(router.urls)),  # nome do app
    path('user/eventos/', EventoView.as_view({'get': 'get_events_by_user'}), name='user-eventos'),

]

