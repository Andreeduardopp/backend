from django.db import migrations
import sys

def add_initial_categories(apps, schema_editor):

    if 'test' in sys.argv:
        return
    
    Categoria = apps.get_model('Eventos', 'Categoria') 

    categorias = ['rock', 'eletronico', 'sertanejo', 'forró','funk','acustico']
    for categoria_nome in categorias:
        Categoria.objects.create(nome=categoria_nome)

class Migration(migrations.Migration):

    dependencies = [
        ('Eventos', '0005_evento_hora_inicio'),
    ]

    operations = [
        migrations.RunPython(add_initial_categories),
    ]