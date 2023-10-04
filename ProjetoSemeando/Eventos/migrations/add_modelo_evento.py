from django.db import migrations
import sys
from django.core.files import File
import os

def criar_evento_modelo(apps, schema_editor):
    
    if 'test' in sys.argv:
        return
    Evento = apps.get_model('Eventos', 'Evento') 
    image_path = "C:/Users/andre/programação/curso/trabalho/Projeto2/backend/ProjetoSemeando/static/Evento_modelo/musica-ao-vivo-na-area.jpg"
    image_file = open(image_path, "rb")
    Evento.objects.create(
        titulo="Exemplo de Evento",
        data="2023-10-05",
        hora_inicio="14:00",
        descricao="Este é um exemplo de evento.",
        valor_entrada=50.00,
        cep="12345678",
        rua="Rua Exemplo",
        numero="123",
        cidade="Cidade Exemplo",
        categoria_id=1,
        foto_principal=File(image_file, os.path.basename(image_path)))
    

class Migration(migrations.Migration):

    dependencies = [
        ('Eventos', 'add_categorias'),
    ]

    operations = [
        migrations.RunPython(criar_evento_modelo),
    ]