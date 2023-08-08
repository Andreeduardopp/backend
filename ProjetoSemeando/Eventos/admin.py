
from django.contrib import admin
from Eventos.models import Evento, Categoria

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    # campos que vão aparecer na listagem
    list_display = ('id', 'titulo', 'data','descricao','valor_entrada','data_postagem',
                   'foto_principal','categoria','cep','rua','numero','cidade')


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    # campos que vão aparecer na listagem
    list_display = ('id', 'nome')